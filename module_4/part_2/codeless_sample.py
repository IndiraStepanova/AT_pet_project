{
  "id": "9433c288-2f29-4e31-9482-5b56c98eb3c2",
  "version": "2.0",
  "name": "codeless_sample",
  "url": "http://selenium1py.pythonanywhere.com",
  "tests": [{
    "id": "703c6407-a37c-4584-b23a-87d069745d74",
    "name": "test_reg",
    "commands": [{
      "id": "1b968ab1-b134-4008-b530-82b4795aa20f",
      "comment": "",
      "command": "open",
      "target": "/ru/",
      "targets": [],
      "value": ""
    }, {
      "id": "cdb013c6-a9da-44c2-bdfd-cd13c6adeb88",
      "comment": "",
      "command": "setWindowSize",
      "target": "1218x824",
      "targets": [],
      "value": ""
    }, {
      "id": "2e69c8d6-2d2b-432a-9ef3-4298034966a7",
      "comment": "",
      "command": "click",
      "target": "id=login_link",
      "targets": [
        ["id=login_link", "id"],
        ["linkText=Войти или зарегистрироваться", "linkText"],
        ["css=#login_link", "css:finder"],
        ["xpath=//a[contains(text(),'Войти или зарегистрироваться')]", "xpath:link"],
        ["xpath=//a[@id='login_link']", "xpath:attributes"],
        ["xpath=//div[@id='top_page']/div[2]/div/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/ru/accounts/login/')]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,' Войти или зарегистрироваться')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "4455f053-70bb-4a0d-8bb9-aab434031d8a",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-email",
      "targets": [
        ["id=id_registration-email", "id"],
        ["name=registration-email", "name"],
        ["css=#id_registration-email", "css:finder"],
        ["xpath=//input[@id='id_registration-email']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div/div/input", "xpath:position"]
      ],
      "value": "NameLastname@email.com"
    }, {
      "id": "09383644-b0b5-4293-aa97-d860749ea9b7",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-password1",
      "targets": [
        ["id=id_registration-password1", "id"],
        ["name=registration-password1", "name"],
        ["css=#id_registration-password1", "css:finder"],
        ["xpath=//input[@id='id_registration-password1']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5b46b5ce-a998-4283-b4a1-a17bfa207bd6",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password1",
      "targets": [
        ["id=id_registration-password1", "id"],
        ["name=registration-password1", "name"],
        ["css=#id_registration-password1", "css:finder"],
        ["xpath=//input[@id='id_registration-password1']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div[2]/div/input", "xpath:position"]
      ],
      "value": "!2wsxCDE#"
    }, {
      "id": "78a39153-77dc-4f2d-be5a-230a3cb5d7a3",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "27c9020e-cf7a-48c1-97a8-c3499db59bba",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": "!2wsxCDE#"
    }, {
      "id": "535cc3e2-cf62-40c0-b91c-25330c08f0e5",
      "comment": "",
      "command": "click",
      "target": "name=registration_submit",
      "targets": [
        ["name=registration_submit", "name"],
        ["css=#register_form > .btn", "css:finder"],
        ["xpath=//button[@name='registration_submit']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/button", "xpath:idRelative"],
        ["xpath=//div[2]/form/button", "xpath:position"],
        ["xpath=//button[contains(.,'Зарегистрироваться')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "073e47cc-ff51-4114-8312-b85a6778fd05",
      "comment": "",
      "command": "click",
      "target": "css=.collapse > div > ul > li:nth-child(1) > a",
      "targets": [],
      "value": ""
    }, {
      "id": "98bf6515-cb7d-499a-a94d-33cb55ddd443",
      "comment": "",
      "command": "assertText",
      "target": "css=div > table > tbody :nth-child(2) > td",
      "targets": [
        ["name=login_submit", "name"],
        ["css=.btn:nth-child(7)", "css:finder"],
        ["xpath=//button[@name='login_submit']", "xpath:attributes"],
        ["xpath=//form[@id='login_form']/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/form/button", "xpath:position"],
        ["xpath=//button[contains(.,'Войти')]", "xpath:innerText"]
      ],
      "value": "NameLastname@email.com"
    }]
  }],
  "suites": [{
    "id": "0079120f-796f-4a44-b09d-0d1e53fad07b",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["703c6407-a37c-4584-b23a-87d069745d74"]
  }],
  "urls": ["http://selenium1py.pythonanywhere.com/"],
  "plugins": []
}