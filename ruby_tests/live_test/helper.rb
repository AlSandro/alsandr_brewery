require 'capybara'
require 'selenium-webdriver'
require 'capybara/rspec'
require 'capybara-screenshot/rspec'

ENV['REMOTE_HOST'] = 'https://worksense.development.daqri.info'

if ENV['REMOTE_HOST'] != ''
  Capybara.app_host = ENV['REMOTE_HOST']
else
  Capybara.server_host = '0.0.0.0'
  Capybara.server_port = '3030'
  Capybara.app_host = 'https://app-proxy'
end

Capybara.register_driver :selenium do |app|
  selenium_hub = 'http://firefox:4444/wd/hub'
  if ENV['BROWSER'] == 'Firefox'
    profile = Selenium::WebDriver::Firefox::Profile.new
    profile['media.navigator.permission.disabled'] = true
    profile['media.navigator.streams.fake'] = true
    # caps = Selenium::WebDriver::Remote::Capabilities.new(accept_insecure_certs: true)
    capabilities = Selenium::WebDriver::Remote::Capabilities.firefox(acceptInsecureCerts: true)
    options = Selenium::WebDriver::Firefox::Options.new
    options.profile = profile
    Capybara::Selenium::Driver.new(app,
                                   browser: :firefox,
                                   url: selenium_hub,
                                   options: options,
                                   desired_capabilities: capabilities)
  else
    selenium_hub = 'http://chrome:4444/wd/hub'
    capabilities = Selenium::WebDriver::Remote::Capabilities.chrome(
      'goog:chromeOptions' => { args: %w[disable-web-security allow-running-insecure-content disable-gpu no-sandbox verbose use-fake-ui-for-media-stream use-fake-device-for-media-stream allow-file-access-from-files] },
      'browserName' => 'chrome'
    )
    Capybara::Selenium::Driver.new(app,
                                   browser: :chrome,
                                   url: selenium_hub,
                                   desired_capabilities: capabilities)
  end
end

# Selenium::WebDriver.logger.level = :warn

Capybara.javascript_driver = :selenium
# Capybara.run_server = false

Capybara::Screenshot.autosave_on_failure = true
Capybara::Screenshot.prune_strategy = :keep_last_run

Capybara.configure do |config|
  config.default_max_wait_time = 30 # seconds
  config.default_driver        = :selenium
end

RSpec.configure do |config|
  # config.filter_gems_from_backtrace("gem name")
  config.before(:each, type: :feature) do
    puts page.evaluate_script('window.navigator.userAgent')
    puts page.evaluate_script('window.navigator.platform')
    Capybara.current_session.driver.browser.manage.window.resize_to(1440, 900)
  end

  #   # Allows RSpec to persist some state between runs in order to support
  #   # the `--only-failures` and `--next-failure` CLI options. We recommend
  #   # you configure your source control system to ignore this file.
  config.example_status_persistence_file_path = 'spec/examples.txt'

  #   # Print the 10 slowest examples and example groups at the
  #   # end of the spec run, to help surface which specs are running
  #   # particularly slow.
  config.profile_examples = 10
  #
  #   # Run specs in random order to surface order dependencies. If you find an
  #   # order dependency and want to debug it, you can fix the order by providing
  #   # the seed, which is printed after each run.
  #   #     --seed 1234
  config.order = :defined
end

