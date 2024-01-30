import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_screenshot(driver, filename):
    driver.save_screenshot(filename)
    print(f"Captured screenshot: {filename}")
def click_on_space(driver, space_number_str):
    space_number = int(space_number_str)  # Convert the string to an integer
    xpath = f"//img[@name='space{space_number_str.zfill(2)}']"  # Ensure the space number is formatted as a two-digit string
    target_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    target_element.click()
    

def test_select_piece_and_move():
    # Test Case: Select Piece and Move
    print("Test Case: Select Piece and Move")
    # Open the specified URL
    driver.get("https://www.gamesforthebrain.com/game/checkers/")
    click_on_space(driver, "02")
    click_on_space(driver, "13")
    # Add a static wait of 5 seconds to observe changes
    time.sleep(5)
    actual_text = driver.find_element(By.XPATH, "//p[@id='message']").text
    expected_text = "Make a move."
    assert actual_text == expected_text, f"Assertion Failed: Expected '{expected_text}', but got '{actual_text}'"


def test_invalid_move():
    # Define the test case
    print("Test Case: Invalid Move")

    # Click on the initial piece (assuming this action)
    click_on_space(driver, "13")
    click_on_space(driver, "02")
    # Wait for the initial element to check its src attribute
    initial_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@name='space02']"))
    )

    # Check if the src attribute is equal to the expected value
    expected_src = "https://www.gamesforthebrain.com/game/checkers/gray.gif"
    actual_src = initial_element.get_attribute("src")

    if actual_src == expected_src:
        print("Test Case Successful: Invalid Move - Initial piece is at the expected location.")
    else:
        print(f"Test Case Failed: Invalid Move - Initial piece is not at the expected location. Actual src: {actual_src}")

def test_lose_move():
    # Define the test case
    print("Test Case: Lose Move")
    time.sleep(5)
    # Click on the initial piece (assuming this action)
    click_on_space(driver, "22")
    
    # Click on the target element
    click_on_space(driver, "33")
    # Check if my checker got eaten
    actual_src = initial_element.get_attribute("src")
    expected_src = "https://www.gamesforthebrain.com/game/checkers/me1.gif"
    partial_src = "me1.gif"
    initial_element_xpath = f"//img[@name='space02' and contains(@src, '{partial_src}')]"

    initial_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, initial_element_xpath))
)

    if actual_src == expected_src:
        print("Test Case Successful: I lose a checker")
    else:
        print(f"Test Case Failed: I didn't lose Actual src: {actual_src}")


if __name__ == "__main__":
    # driver
    driver = webdriver.Edge()

    try:
        # Initialize and run the test cases
        test_select_piece_and_move()
        capture_screenshot(driver, "screenshot_after_first_test.png")

        test_invalid_move()
        capture_screenshot(driver, "screenshot_after_another_test.png")
        test_lose_move()

    finally:
        # Close the browser window
        driver.quit()
