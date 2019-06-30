def wait_for_text(txt, max = 5)
  wait_until(max) do
    expect(page.text).to match(/#{txt}/)
  end
end

def wait_for_visible_element(selector, max = 5)
  wait_until(max) do
    expect(page).to have_selector(selector, visible: true)
  end
end

def wait_until(max = 5, wait_time = 0.25)
  start = Time.now.to_f
  begin
    yield
  rescue RSpec::Expectations::ExpectationNotMetError => e
    if (Time.now - start).to_f > max
      puts "== waited max #{max} seconds" if ENV['VERBOSE'] == 'true'
      raise e
    else
      sleep(wait_time)
      retry
    end
  rescue Exception => e
    if (Time.now - start).to_f > max
      puts "== waited max #{max} seconds" if ENV['VERBOSE'] == 'true'
      raise e
    else
      sleep(wait_time)
      retry
    end
  end
end
def wait_for_text(txt, max = 5)
  wait_until(max) do
    expect(page.text).to match(/#{txt}/)
  end
end

def upload_file_drag_drop(id, file)
  Capybara.ignore_hidden_elements = false
  inp = page.find("##{id}").find('input')
  inp.set(file)
  Capybara.ignore_hidden_elements = true
end
