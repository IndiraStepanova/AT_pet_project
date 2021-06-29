from ..base_page import BasePage
from ..locators import AccountPageLocators


expected_profile_page_header_button_text = {
    "ru": "Профиль",
    "en-gb": "Profile",
    "fr": "Profil",
    "es": "Perfil",
}

expected_change_password_button_text = {
    "ru": "Изменить пароль",
    "en-gb": "Change password",
    "fr": "Modifier le mot de passe",
    "es": "Cambiar contraseña",
}

expected_edit_profile_button_text = {
    "ru": "Редактировать профиль",
    "en-gb": "Edit profile",
    "fr": "Modifier le profil",
    "es": "Editar perfil",
}

expected_delete_profile_button_text = {
    "ru": "Удалить профиль",
    "en-gb": "Delete profile",
    "fr": "Supprimer le profil",
    "es": "Eliminar perfil",
}


class AccountPage(BasePage):
    def should_be_main_account_page(self, language):
        self.should_be_profile_url()
        self.should_be_profile_page_header(language)
        self.should_be_password_change_link(language)
        self.should_be_edit_profile_link(language)
        self.should_be_delete_profile_link(language)

    def should_be_profile_url(self):
        assert "accounts/profile" in self.browser.current_url, "It is not account URL!"

    def should_be_profile_page_header(self, language):
        account_page_header = self.get_element_text(
            *AccountPageLocators.ACCOUNT_PAGE_HEADER)
        assert account_page_header in expected_profile_page_header_button_text[
            language], "Header of page does not match to locale!"

    def should_be_password_change_link(self, language):
        change_password_button_text = self.get_element_text(
            *AccountPageLocators.CHANGE_PASSWORD_BUTTON)
        assert change_password_button_text in expected_change_password_button_text[
            language], "'Change password' button text does not match to locale!"
        assert self.is_element_present(
            *AccountPageLocators.CHANGE_PASSWORD_BUTTON), "Change password button is not presented!"
        assert self.is_element_clicable(
            *AccountPageLocators.CHANGE_PASSWORD_BUTTON), "Change password button is not clicable!"

    def should_be_edit_profile_link(self, language):
        edit_profile_button_text = self.get_element_text(
            *AccountPageLocators.EDIT_PROFILE_BUTTON)
        assert edit_profile_button_text in expected_edit_profile_button_text[
            language], "'Edit profile' button text does not match to locale!"
        assert self.is_element_present(
            *AccountPageLocators.EDIT_PROFILE_BUTTON), "Edit profile button is not presented!"
        assert self.is_element_clicable(
            *AccountPageLocators.EDIT_PROFILE_BUTTON), "Edit profile button is not clicable!"

    def should_be_delete_profile_link(self, language):
        delete_profile_button_text = self.get_element_text(
            *AccountPageLocators.DELETE_PROFILE_BUTTON)
        assert delete_profile_button_text in expected_delete_profile_button_text[
            language], "'Delete_profile' button text does not match to locale!"
        assert self.is_element_present(
            *AccountPageLocators.DELETE_PROFILE_BUTTON), "Delete profile button is not presented!"
        assert self.is_element_clicable(
            *AccountPageLocators.DELETE_PROFILE_BUTTON), "Delete profile button is not clicable!"

    def go_to_change_password_page(self):
        link = self.browser.find_element(
            *AccountPageLocators.CHANGE_PASSWORD_BUTTON)
        link.click()

    def go_to_edit_profile_page(self):
        link = self.browser.find_element(
            *AccountPageLocators.EDIT_PROFILE_BUTTON)
        link.click()

    def go_to_delete_profile_page(self):
        link = self.browser.find_element(
            *AccountPageLocators.DELETE_PROFILE_BUTTON)
        link.click()

    def should_be_success_message(self):
        assert self.is_element_present(*AccountPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AccountPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be!"
    
    def user_can_logout(self):
        self.go_to_logout_link()