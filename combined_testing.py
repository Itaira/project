import backend_testing
import frontend_testing
import time

user = "testing_user"
update_to_user = "testing_update_user"
index = "999"
xpath = "/html/body/pre"

print("TEST 1: ")
backend_testing.create_user_testing(user, index)
time.sleep(2)

print("TEST 2: ")
backend_testing.check_user_db_testing(user, index)
time.sleep(2)

print("TEST 3: ")
backend_testing.update_user_testing(update_to_user, index)
time.sleep(2)

print("TEST 4: ")
backend_testing.get_user_testing(index)
time.sleep(2)

print("TEST 5: ")
driver, locator = frontend_testing.start_selenium(index, xpath)
time.sleep(2)

print("TEST 6: ")
frontend_testing.print_connection_testing(driver)
time.sleep(2)

print("TEST 7: ")
frontend_testing.check_element_exists_testing(driver, locator)
time.sleep(2)

print("TEST 8: ")
frontend_testing.print_user_testing(driver, locator)
time.sleep(2)

print("TEST 9: ")
backend_testing.delete_user_testing(index)
time.sleep(2)

print("TEST 10: ")
backend_testing.check_user_db_testing(user, index)
