from .account_page import AccountPage
from ..locators import ChangePasswordPageLocators

expected_change_password_button_text = {
    "ru": "Изменить пароль",
    "en-gb": "Change password",
    "fr": "Modifier le mot de passe",
    "es": "Cambiar contraseña",
}


class ChangePasswordPage(AccountPage):
    def should_be_change_password_page_url(self):
        assert "accounts/change-password" in self.browser.current_url, "It is not change password page URL!"

    def should_be_fields_for_changing_password(self, old_password, new_password):
        old_password_input = self.browser.find_element(
            *ChangePasswordPageLocators.OLD_PASSWORD)
        old_password_input.send_keys(old_password)
        new_password_input = self.browser.find_element(
            *ChangePasswordPageLocators.NEW_PASSWORD)
        new_password_input.send_keys(new_password)
        new_password_confirmation_input = self.browser.find_element(
            *ChangePasswordPageLocators.NEW_PASSWORD_CONFIRMATION)
        new_password_confirmation_input.send_keys(new_password)

    def user_can_save_changed_password(self):
        change_password_submit_button = self.browser.find_element(
            *ChangePasswordPageLocators.CHANGE_PASSWORD_SUBMIT)
        change_password_submit_button.click()

    def user_can_cancel_of_changing_password(self):
        change_password_cancel_button = self.browser.find_element(
            *ChangePasswordPageLocators.CHANGE_PASSWORD_CANCEL)
        change_password_cancel_button.click()
