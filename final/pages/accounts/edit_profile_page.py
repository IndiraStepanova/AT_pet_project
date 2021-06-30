from .account_page import AccountPage
from ..locators import EditProfilePageLocators

expected_edit_profile_header = {
    "ru": "Редактировать профиль",
    "en-gb": "Edit Profile",
    "fr": "Modifier le profil",
    "es": "Editar perfil",
}


class EditProfilePage(AccountPage):
    def should_be_edit_profile_page_url(self):
        assert "accounts/profile/edit/" in self.browser.current_url, "It is not edit profile page URL!"

    def should_be_edit_profile_page_header(self, language):
        edit_profile_page = self.get_element_text(
            *EditProfilePageLocators.EDIT_PROFILE_PAGE_HEADER)
        assert edit_profile_page in expected_edit_profile_header[
            language], "Header of edit profile page does not match to locale!"

    def should_be_fields_for_edit_profile(self, new_name, new_surname, new_email):
        new_name_input = self.browser.find_element(
            *EditProfilePageLocators.NEW_NAME)
        new_name_input.send_keys(new_name)
        new_surname_input = self.browser.find_element(
            *EditProfilePageLocators.NEW_LASTNAME)
        new_surname_input.send_keys(new_surname)
        new_email_input = self.browser.find_element(
            *EditProfilePageLocators.NEW_EMAIL)
        new_email_input.send_keys(new_email)

    def user_can_save_changes_for_profile(self):
        edit_profile_submit_button = self.browser.find_element(
            *EditProfilePageLocators.EDIT_PROFILE_SUBMIT)
        edit_profile_submit_button.click()

    def user_can_cancel_changes_for_profile(self):
        edit_profile_cancel_button = self.browser.find_element(
            *EditProfilePageLocators.EDIT_PROFILE_CANCEL)
        edit_profile_cancel_button.click()
