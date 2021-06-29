from .account_page import AccountPage
from ..locators import DeleteProfilePageLocators


class DeleteProfilePage(AccountPage):
    def should_be_edit_profile_page_url(self):
        assert "accounts/profile/delete/" in self.browser.current_url, "It is not delete profile page URL!"

    def should_be_password_field_for_delete_profile(self, user_password):
        user_password_input = self.browser.find_element(
            *DeleteProfilePageLocators.USER_PASSWORD)
        user_password_input.send_keys(user_password)
        
    def user_can_submit_delete_profile(self):
        edit_profile_submit_button = self.browser.find_element(
            *DeleteProfilePageLocators.DELETE_PROFILE_SUBMIT)
        edit_profile_submit_button.click()

    def user_can_cancel_delete_profile(self):
        edit_profile_cancel_button = self.browser.find_element(
            *DeleteProfilePageLocators.DELETE_PROFILE_CANCEL)
        edit_profile_cancel_button.click()
