from selenium.webdriver.common.by import By


class Locators():
    AutoComplete = By.XPATH, '//a[@class="btn btn-lg"]'
    Address = By.XPATH, '//input[@id="autocomplete"]'
    Street_address = By.XPATH, '//input[@id="street_number"]'
    Street_address_2 = By.XPATH, '//input[@id="route"]'
    City = By.XPATH, '//input[@id="locality"]'
    State = By.XPATH, '//input[@placeholder="State"]'
    Zip_Code = By.XPATH, '//input[@id="postal_code"]'
    Country = By.XPATH, '//input[@id="country"]'

    Buttons = By.XPATH, '(//a[@class="btn btn-lg"])[2]'
    PrimaryButton = By.XPATH, '//button[@class="btn btn-lg btn-primary"]'
    SuccessButton = By.XPATH, '//button[@class="btn btn-lg btn-success"]'
    InfoButton = By.XPATH, '//button[@fdprocessedid="eyfe7l"]'
    WarningButton = By.XPATH, '//button[@class="btn btn-lg btn-warning"]'
    DangerButton = By.XPATH, '//button[@fdprocessedid="qe6h9"]'
    LinkButton = By.XPATH, '//button[@fdprocessedid="qzfgew"]'
    LeftButton = By.XPATH, '(//button[@class="btn btn-lg btn-primary"])[2]'
    MiddleButton = By.XPATH, '(//button[@class="btn btn-lg btn-primary"])[3]'
    RightButton = By.XPATH, '(//button[@class="btn btn-lg btn-primary"])[4]'
    OneButton = By.XPATH, '(//button[@class="btn btn-lg btn-primary"])[5]'
    TwoButton = By.XPATH, '(//button[@class="btn btn-lg btn-primary"])[6]'
    Drop_down = By.ID, 'btnGroupDrop1'
    Drop_down_link_1 = By.XPATH,'(//a[@class="dropdown-item"])[15]'
    Drop_down_link_2 = By.XPATH, '(//a[@class="dropdown-item"])[16]'

    CheckBox = By.XPATH, '(//a[@class="btn btn-lg"])[3]'
    Checkbox1 = By.ID, 'checkbox-1'
    Checkbox2 = By.ID, "checkbox-2"
    Checkbox3 = By.ID, "checkbox-3"

    Datepicker = By.XPATH, '(//a[@class="btn btn-lg"])[4]'
    Date = By.XPATH, '//input[@id="datepicker"]'

    DragAndDrop = By.XPATH, '(//a[@class="btn btn-lg"])[5]'
    # source_location = By.ID, 'image'
    # destination_location = By.ID, 'box'

    # https: // www.globalsqa.com / demo - site / draganddrop /
    source_location = By.XPATH, '//ul[@id="gallery"]/li[4]'
    destination_location = By.ID, 'trash'
    iframe = By.XPATH, '//iframe[@class="demo-frame lazyloaded"]'

    DropDown = By.XPATH, '(//a[@class="btn btn-lg"])[6]'
    DropDownButton = By.XPATH, '//button[@id="dropdownMenuButton"]'
    check_box = By.XPATH,'(//a[@class="dropdown-item"])[17]'

    Enabled_and_disable_element = By.XPATH, '(//a[@class="btn btn-lg"])[7]'
    inputHere = By.XPATH, '//input[@id="input"]'

    FileUpload = By.XPATH, '(//a[@class="btn btn-lg"])[8]'
    choose = By.ID,'file-upload-field'

    key_and_mouse_press = By.XPATH, '(//a[@class="btn btn-lg"])[9]'
    full_name = By.XPATH, '//input[@id="name"]'
    button_name = By.XPATH, '//button[@id="button"]'

    Modal = By.XPATH, '(//a[@class="btn btn-lg"])[10]'
    OpenModel = By.XPATH, '//button[@id="modal-button"]'
    CloseButton = By.XPATH, '//button[@id="close-button"]'

    PageScroll = By.XPATH, '(//a[@class="btn btn-lg"])[11]'
    FullName = By.XPATH, '//input[@id="name"]'
    date = By.XPATH, '//input[@id="date"]'

    RadioButton = By.XPATH, '(//a[@class="btn btn-lg"])[12]'
    RadioButton1 = By.ID, 'radio-button-1'
    RadioButton2 = By.XPATH, '(//label[@class="form-check-label"])[2]'
    RadioButton3 = By.XPATH, '(//label[@class="form-check-label"])[3]'

    SwitchWindow = By.XPATH, '(//a[@class="btn btn-lg"])[13]'
    OpenNewTab = By.XPATH, '//button[@id="new-tab-button"]'
    OpenAlert = By.XPATH, '//button[@id="alert-button"]'

    CompleteWebForm = By.XPATH, '(//a[@class="btn btn-lg"])[14]'
    FirstName = By.XPATH, '//input[@id="first-name"]'
    LastName = By.XPATH, '//input[@id="last-name"]'
    Job_title = By.XPATH, '//input[@id="job-title"]'
    HighSchool = By.ID, 'radio-button-1'
    College = By.ID, 'radio-button-2'
    GrabSchool = By.ID, 'radio-button-3'
    Male = By.ID, 'checkbox-1'
    Female = By.ID, 'checkbox-2'
    Not_prefer = By.ID, 'checkbox-3'
    Experience = By.ID,'select-menu'
    date_1 = By.XPATH, '//input[@id="datepicker"]'
    Click_on_submit_button = By.XPATH, '//a[@class="btn btn-lg btn-primary"]'
