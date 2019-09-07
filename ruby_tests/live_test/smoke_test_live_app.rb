require '/srv/test/helper'
require '/srv/test/utilities'

RSpec.feature 'Calls', type: :feature do

  scenario 'A user should be able to make a call', js: true do
    puts '====*********** SHOW APP > SANITY TEST STARTED ***********===='
    visit '/show/#/'
    
    page.find('#sign-in-link').click

    @smoke_user = "superuser@daqri.com"
    @smoke_key = "toaster"

    fill_in 'login_username', with: @smoke_user
    fill_in 'login_password', with: @smoke_key
    page.find('#login-go').click

    puts page.text

    puts '==== User A logged in. User A is happy!!! ===='
    wait_for_text('Super User')
    wait_until do
      page.find('#settings-button').click
      expect(page.text).to match(/OUTGOING VIDEO QUALITY/)
    end
    puts '==== User changes settings to all calls to pre-call test. User A is happy!!! ===='
    
    click_on('All calls')
    page.all('.resolution')[1].click
    page.all('.fps')[1].click

    page.first('#back-link').click

    Capybara.using_session_with_screenshot('same_user') do
      puts '==== User started new session in a separate window. User A is happy!!! ===='
      visit '/show/#/'
      page.find('#sign-in-link').click

      fill_in 'login_username', with: @smoke_user
      fill_in 'login_password', with: @smoke_key
      page.find('#login-go').click

      wait_for_text('Super User')
      

      page.find('#title-link').click
      expect(page.text).to match(/SHOW PROFILE/)
      # First, upload an avatar, not for FF though
      # wait_until do
      #   upload_file_drag_drop('avatar-upload', '/srv/test/data/avatar.png')
      # end
      # wait_for_text('Avatar successfully updated')

      puts '==== User changes the avatar. User A is happy!!! ===='

      # Next, set job title
      sleep 0.1
      Capybara.ignore_hidden_elements = false
      page.find('.pen-css-label').click
      # page.evaluate_script("angular.element('#checkbox-title').click()") # Click w/ javascript since it's hidden
      fill_in 'user-job-title', with: 'Job Title'
      Capybara.ignore_hidden_elements = true

      page.find('#save-title').click

      puts '==== User changes the job title. User A is happy!!! ===='
    end

    wait_until do
      page.first('.user-call').click
    end

    puts '==== User playing with the the pre-call test. User A is happy!!! ===='
    # Video switch
    wait_for_visible_element('.OT_video-element')
    page.find('#switch-video').click
    wait_for_visible_element('.OT_video-poster')
    page.find('#switch-video').click
    wait_for_visible_element('.OT_video-element')

    # Audio switch
    wait_until do
      expect(page.evaluate_script("angular.element('#audio-meter-level').outerWidth()")).to_not eql(0)
    end
    page.find('#switch-audio').click
    expect(page.evaluate_script("angular.element('#audio-meter-level').outerWidth()")).to eql(0)
    page.find('#switch-audio').click

    wait_for_visible_element('#results-panel', 45)

    wait_for_text('Test complete')
    puts '==== Test complete, the User is happy. User A is happy!!! ===='


    page.find('.dq-css-label').click

    # save_and_open_screenshot
    page.find('#continue-to-call').click

    # The call itself: publisher
    wait_for_text('Connecting your call')

    Capybara.using_session_with_screenshot('same_user') do
      # Show the 'incoming call' screen
      wait_for_text('Incoming Call')

      page.find('#accept-call').click

      wait_for_text('END CALL')
      # The call itself: publisher
      wait_for_visible_element('.main')
      wait_for_visible_element('.streamers')
    end

    # The call itself: publisher
    wait_for_visible_element('.main')
    wait_for_visible_element('.streamers')

    expect(page.text).to_not match(/Connecting your call/)

    puts '==== User A calling to user A. Users A are happy!!!===='
    # Test video enable/disable
    wait_until do
      expect(page).to have_selector('.OT_video-poster', visible: false, count: 2)
    end
    page.find('#toggle-video').click
    wait_until do
      expect(page).to have_selector('.OT_video-poster', visible: true, count: 1)
    end
    page.find('#toggle-video').click
    wait_until do
      expect(page).to have_selector('.OT_video-poster', visible: false, count: 2)
    end
    puts '==== User playing with the video on and off. User A is happy!!!===='

    # Test toggle screenshot annotations
    page.find('#toggle-screenshot').click

    wait_until do
      expect(page).to have_selector('#back-freeze', visible: true, count: 1)
    end

    wait_until do
      expect(page).to have_selector('.screenshot-annotations', visible: true, count: 1)
      # one whiteboard is the draw board for annotations another is the live view
      expect(page).to have_selector('.whiteboard', visible: true, count: 2)
      # the element is the self camera feed, should still be only one
      expect(page).to have_selector('.OT_mirrored', visible: true, count: 1)
    end

    page.find('#back-freeze').click
    wait_until do
      # back to only one whiteboard for live annotations
      expect(page).to have_selector('.whiteboard', visible: true, count: 1)
    end
    puts '==== User playing with the freeze frame. User A is happy!!! ===='


    # Test call stats
    page.find('#toggle-call-stats').click
    wait_for_text('Call Statistics')
    page.find('#toggle-call-stats').click

    puts '==== User checking call statistics. User A is happy!!! ===='
    
    page.find('#hang-up').click

    # Back to contacts screen: publisher
    wait_for_visible_element('#contacts')

    # Back to contacts screen: subscriber
    Capybara.using_session_with_screenshot('same_user') do
      wait_for_text('Super User')
      wait_for_visible_element('#settings-button')
    end
    puts '==== User A hang-up and do not see User A anymore. User A is happy!!! ===='
    puts '====*********** SHOW APP > SANITY TEST FINISHED *************===='
  end
end
