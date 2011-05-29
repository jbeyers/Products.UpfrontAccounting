from Products.Archetypes.utils import DisplayList
from Products.CMFCore.permissions import setDefaultRoles
DEPENDENCIES = ['FinanceFields',]

STATEMENT_CSV_KEY = 'statement_csv_file' # for saving statement csv data in session variable

# Permissions
PostTransaction = 'PA: PostTransaction'
PostInvoice = 'PA: PostInvoice'
PostCreditNote = 'PA: PostCreditNote'
PostCashBook = 'PA: PostCashBook'
ManageAccounts = 'PA: Manage Accounts'
ManageCashBook = 'PA: Manage Cashbook'
ManageTransactions = 'PA: Manage Transactions'
ManageInvoices = 'PA: Manage Invoices'
ManageQuotes = 'PA: Manage Quotes'
ManageCreditNotes = 'PA: Manage CreditNotes'
UndoTransaction = 'UpfrontAccounting: undo transaction'

setDefaultRoles(UndoTransaction, ('Manager', 'Owner'))

ACCOUNT_TYPES = ('Asset', 'Liability', 'Equity', 'Income', 'Expense',)

BALANCE_SHEET_SECTIONS = DisplayList((
    ('','Not applicable'),
    ('B10','Retained Income'),
    ('B25','Long Term Liabilities'),
    ('B30','Other Long Term Liabilities'),
    ('B35','Fixed Assets'),
    ('B40','Investments'),
    ('B45','Other Fixed Assets'),
    ('B50','Inventory'),
    ('B55','Accounts Receivable'),
    ('B60','Bank'),
    ('B65','Other Current Assets'),
    ('B70','Accounts Payable'),
    ('B80','Other Current Liabilities'),
))

INCOME_STATEMENT_SECTIONS = DisplayList((
    ('','Not applicable'),
    ('I10','Sales'),
    ('I15','Cost of Sales'),
    ('I20','Other Income'),
    ('I25','Expenses'),
    ('I30','Tax'),
    ('I35','Dividends'),
))

DEBIT = 'Debit'
CREDIT = 'Credit'
INCOME = 'Income'
EXPENSE = 'Expense'

CannotModifyControlAccount = "Cannot modify control account"

RECURRENCE = DisplayList((
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
))

BANK_ACCOUNT_TYPES = DisplayList((
    ('savings', 'Savings'),
    ('cheque', 'Cheque'),
    ('credit', 'Credit card'),
    ('loan', 'Home loan'),
    ))

COUNTRY_NAMES = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antarctica",
    "Antigua Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia Herzegovina",
    "Botswana",
    "Bouvet Island",
    "Brazil",
    "British Indian Ocean Territory",
    "Brunei Darussalam",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "Congo, Democratic Republic",
    "Cook Islands",
    "Costa Rica",
    "Cote D'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands (Malvinas)",
    "Faroe Islands",
    "Fiji",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "French Southern Territories",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guam",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Heard Island Mcdonald Islands",
    "Holy See (Vatican City State)",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran, Islamic Republic",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, Democratic People's Republic",
    "Korea, Republic",
    "Kuwait",
    "Kyrgyzstan",
    "Lao People's Democratic Republic",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libyan Arab Jamahiriya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "Macedonia, Former Yugoslav Republic",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia, Federated States",
    "Moldova, Republic",
    "Monaco",
    "Mongolia",
    "Montserrat",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "Netherlands Antilles",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norfolk Island",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestinian Territory, Occupied",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Pitcairn",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Reunion",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Helena",
    "Saint Kitts Nevis",
    "Saint Lucia",
    "Saint Pierre Miquelon",
    "Saint Vincent Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Georgia South Sandwich Islands",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Svalbard Jan Mayen",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syrian Arab Republic",
    "Taiwan, Province China",
    "Tajikistan",
    "Tanzania, United Republic",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "United States Minor Outlying Islands",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Virgin Islands, British",
    "Virgin Islands, U.S.",
    "Wallis Futuna",
    "Western Sahara",
    "Yemen",
    "Zambia",
    "Zimbabwe",
    ]