class Language:
    MENU = ".//*[@id='mailRuToolbar']/table/tbody/tr/td[2]/div/span/span[1]"
    RU = ".//*[@id='mailRuToolbar']/table/tbody/tr/td[2]/div/div/div/a[1]"
    EN = ".//*[@id='mailRuToolbar']/table/tbody/tr/td[2]/div/div/div/a[1]"


class Credentials:
    LOGIN = ".//*[@id='field_email']"
    PASSWORD = ".//*[@id='field_password']"
    SUBMIT_BUTTON = ".//*[@id='loginContentBlock']/form/div[4]/input"


class SettingsPage:
    SETTINGS_DIALOG = ".//*[@id='hook_Block_UserConfigMRB']/div/a[1]"


class SettingsDialog:
    TEXT_FIELDS = {
        "first_name": ".//*[@id='field_name']",
        "last_name": ".//*[@id='field_surname']",
        "current_city": ".//*[@id='field_citySugg_SearchInput']",
        "origin_city": ".//*[@id='field_cityBSugg_SearchInput']",
    }

    SELECT_FIELDS = {
        "day_birthday": ".//*[@id='field_bday']",
        "month_birthday": ".//*[@id='field_bmonth']",
        "year_birthday": ".//*[@id='field_byear']",
    }

    BUTTONS = {
        "submit": ".//*[@id='hook_FormButton_button_savePopLayerEditUserProfileNew']",
        "cancel": ".//*[@id='button_cancelPopLayerEditUserProfileNew']",
        "accept_changes": ".//*[@id='buttonId_button_close']"
    }

    ERROR_FIELDS = {
        'first_name': ".//*[@id='hook_Form_PopLayerEditUserProfileNewForm']/form/div[1]/div[1]/span[2]",
        'ast_name': ".//*[@id='hook_Form_PopLayerEditUserProfileNewForm']/form/div[1]/div[2]/span[2]",
        'birthday': ".//*[@id='hook_Form_PopLayerEditUserProfileNewForm']/form/div[1]/div[3]/span[2]",
        'current_city': ".//*[@id='hook_Form_PopLayerEditUserProfileNewForm']/form/div[1]/div[5]/span",
        'origin_city': ".//*[@id='hook_Form_PopLayerEditUserProfileNewForm']/form/div[1]/div[6]/span",
    }

    GENDER_BUTTONS = {
        "male": ".//*[@id='field_gender_1']",
        "female": ".//*[@id='field_gender_2']"
    }
