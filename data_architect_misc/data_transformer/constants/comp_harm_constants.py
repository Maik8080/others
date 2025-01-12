PROCESSED_DATE_COLUMN = 'PROCESSED_DATE'
YEAR_COLUMN = 'HARMONIZED_YEAR'
MONTH_COLUMN = 'HARMONIZED_MONTH'
DATE_COLUMN = 'HARMONIZED_DATE'
REGION_COLUMN = 'HARMONIZED_REGION'
COUNTRY_COLUMN = 'HARMONIZED_COUNTRY'
ADVERTISER_COLUMN = 'HARMONIZED_ADVERTISER'
MEDIA_TYPE_COLUMN = 'HARMONIZED_MEDIA_TYPE'
CURRENCY_COLUMN = 'HARMONIZED_CURRENCY'
GROSS_SPEND_COLUMN = 'HARMONIZED_GROSS_SPEND'
CATEGORY_COLUMN = 'HARMONIZED_CATEGORY'
SUBCATEGORY_COLUMN = 'HARMONIZED_SUBCATEGORY'
RAW_CATEGORY_COLUMN = 'RAW_CATEGORY'
RAW_SUBCATEGORY_COLUMN = 'RAW_SUBCATEGORY'
RAW_BRAND_COLUMN = 'RAW_BRAND'
RAW_SUBBRAND_COLUMN = 'RAW_SUBBRAND'
RAW_PRODUCT_NAME_COLUMN = 'RAW_PRODUCT_NAME'
RAW_MEDIA_TYPE_COLUMN = 'RAW_MEDIA_TYPE'
PRODUCT_NAME_COLUMN = 'HARMONIZED_PRODUCT_NAME'
NOT_AVAILABLE = 'Not Available'

EXPECTED_COLUMNS = [
    # Standard column names we use in competitive harmonization project
    PROCESSED_DATE_COLUMN,
    YEAR_COLUMN,
    MONTH_COLUMN,
    DATE_COLUMN,
    REGION_COLUMN,
    COUNTRY_COLUMN,
    ADVERTISER_COLUMN,
    MEDIA_TYPE_COLUMN,
    CURRENCY_COLUMN,
    GROSS_SPEND_COLUMN,
    CATEGORY_COLUMN,
    RAW_CATEGORY_COLUMN,
    RAW_SUBCATEGORY_COLUMN,
    RAW_BRAND_COLUMN,
    RAW_SUBBRAND_COLUMN,
    RAW_PRODUCT_NAME_COLUMN,
    SUBCATEGORY_COLUMN,
    PRODUCT_NAME_COLUMN
]

# Below are the regions, countries, categories, media types
# and globally competing advertisers that we support as of April, 2020.
# Whenever we come across new data items for constants below, add them.
REGIONS = {'Africa-Eurasia', 'Asia Pacific', 'Europe', 'Latin America', 'North America'}

COUNTRIES = {
    'Argentina', 'Australia', 'Austria',
    'Bahrain', 'Belgium', 'Brazil',
    'Canada', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Czech Republic',
    'Denmark', 'Dominican Republic',
    'Ecuador', 'El Salvador', 'Estonia',
    'Finland', 'France',
    'Germany', 'Greece', 'Guatemala',
    'Honduras', 'Hong Kong', 'Hungary',
    'India', 'Indonesia', 'Ireland', 'Italy', 'Israel',
    'Kazakhstan', 'Kenya', 'Kuwait',
    'Latvia', 'Lithuania',
    'Malaysia', 'Mexico', 'Morocco',
    'Netherlands', 'New Zealand', 'Nicaragua', 'Norway',
    'Oman',
    'Pan Arab', 'Pan Asian', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico',
    'Qatar',
    'Romania', 'Russia',
    'Saudi Arabia', 'Singapore', 'Slovakia', 'South Africa', 'Spain', 'Sweden', 'Switzerland',
    'Taiwan', 'Thailand', 'Turkey',
    'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'USA',
    'Venezuela', 'Vietnam'
}

MEDIA_TYPES = {'Cinema', 'Digital', 'Door drops', 'In-store', 'OOH', 'Print', 'Radio', 'TV'}

GLOBAL_COMPETE_ADVERTISERS = {
    # This list is used only as a reference for new team members
    # It is not used in the code.
    'BEIERSDORF',
    'CHURCH & DWIGHT',
    'COLGATE-PALMOLIVE',
    'GENOMMA LAB',
    'GSK',
    'HENKEL',
    'JOHNSON & JOHNSON',
    'LOREAL',
    'P&G',
    'PHILIPS',
    'RECKITT BENCKISER',
    'SANOFI',
    'S.C. JOHNSON',
    'THE CLOROX COMPANY',
    'UNILEVER'
}
# On Oct 29, 2020 we decided to distinguish between not available values, which means there is no raw 
# category value in the data file, and the ones which we do not know how to map with Python dictionary.

CATEGORIES = {'Home Care', 'Oral Care', 'Other', 'Personal Care', 'Pet Nutrition', '', NOT_AVAILABLE}

ENGLISH_MEDIA_TYPE_MAPPINGS = {
    "(?i)CINEMA.*": "Cinema",
    "(?i)MAGAZINE.*": "Print",  "(?i)NEWSPAPER.*": "Print", "(?i)JORNAL.*": "Print",  "(?i)PRINT.*": "Print", "(?i)PRESS.*": "Print", "(?i)MG.*": "Print", "(?i)NP.*": "Print",
    "(?i)OUTDOOR.*": "OOH", "(?i)OOH.*": "OOH", "(?i)OUT.*OF.*HOME.*": "OOH","(?i)Bus/Taxis.*":"OOH", "(?i)Posters/Rail/Digital.*":"OOH",
    "(?i)RADIO.*": "Radio", "(?i)RD.*": "Radio",
    "(?i)TV.*": "TV", "(?i)Television.*": "TV", "(?i)SPOTS": "TV", "FTA.*": "TV", "(?i)CABLE.*": "TV", "(?i)CB.*": "TV", "(?i)Pay TV.*": "TV",
    "(?i)DIGITAL.*": "Digital", "(?i)INTERNET.*": "Digital", "(?i)ONLINE.*": "Digital", "(?i)MOBILE.*": "Digital", "(?i)SEARCH.*": "Digital",
}

SPANISH_MEDIA_TYPE_MAPPINGS = {
    "(?i)Televisión.*": "TV", 
    "(?i)PUBLICIDAD\sEXTERIOR.*": "OOH","(?i)VP.*": "OOH","(?i)Vía\sPública.*": "OOH", "(?i)Metro.*": "OOH",
    "(?i)Revista.*": "Print", "(?i)PRENSA.*": "Print", "(?i)DIARIO.*": "Print", "(?i)Suplemento.*": "Print",
}

MEDIA_TYPE_MAPPINGS = dict(ENGLISH_MEDIA_TYPE_MAPPINGS, **SPANISH_MEDIA_TYPE_MAPPINGS)

COUNTRY_MAPPINGS = {
    # Mapping between raw country names in regular expression to standardized country names
    "(?i)BAHRAIN.*": "Bahrain",
    "(?i)KAZAK.*": "Kazakhstan",
    "(?i)KAZAKHSTAN.*": "Kazakhstan",
    "(?i)KENYA.*": "Kenya",
    "(?i)KUWAIT.*": "Kuwait",
    "(?i)KSA.*": "Saudi Arabia",
    "(?i)MOROCCO.*": "Morocco",
    "(?i)MORROCO.*": "Morocco",
    "(?i)MORROCCO.*": "Morocco",
    "(?i)OMAN.*": "Oman",
    "(?i)PAN.*ARAB.*": "Pan Arab",
    "(?i)PAN.*ASIA.*": "Pan Asian",
    "(?i)QATAR.*": "Qatar",
    "(?i)RUSSIA.*": "Russia",
    "(?i)SOUTH.*AFRICA.*": "South Africa",
    "(?i)TURKEY.*": "Turkey",
    "(?i)UKRAINE.*": "Ukraine",
    "(?i)UNITED ARAB EMIRATES.*": "United Arab Emirates",
    "(?i)UAE.*": "United Arab Emirates"
}

ADVERTISER_MAPPINGS = {
    # Mapping between raw advertiser names in regular expression to standardized advertiser names
    # This list will grow to a big one and must be kept maintained/updated constantly.
    "(?i)BDF.*": "BEIERSDORF",
    "(?i).*BEIERSDORF.*": "BEIERSDORF",
    "(?i).*BIERSDORF.*": "BEIERSDORF",
    "(?i).*COLGATE.*": "COLGATE-PALMOLIVE",
    "(?i).*CLOROX.*": "THE CLOROX COMPANY",
    "(?i)^CP$": "COLGATE-PALMOLIVE",
    "(?i)GENOMMA.*": "GENOMMA LAB",
    "(?i).*GLAXO.*": "GSK",  # also catches "\u200EGlaxoSmithKline"
    "(?i)^GSK.*": "GSK",
    "(?i).*HENKEL.*": "HENKEL",
    "(?i).*JOHNSON.*&.*JOHNSON.*": "JOHNSON & JOHNSON",
    "(?i)J.*&.*J.*": "JOHNSON & JOHNSON",
    "(?i).*L'?OREAL.*": "LOREAL",  # also catches 'LOREAL'
    "(?i).*PHILIPS.*": "PHILIPS",
    "(?i).*PROCTER.*&.*GAMBLE.*": "P&G",
    "(?i).*PROCTER.*AND.*GAMBLE.*": "P&G",
    "(?i)P.*&.*G.*": "P&G",
    "(?i).*RECKIT(T)?.*": "RECKITT BENCKISER",
    "(?i)^RB\\s*?$": "RECKITT BENCKISER",
    "(?i)^RB\\sAG$": "RECKITT BENCKISER",
    "(?i)SANOFI.*": "SANOFI",
    "(?i)S(.)?C(.)? JOHNSON.*": "JOHNSON & JOHNSON",
    "(?i).*UNILEVER.*": "UNILEVER"
}

ENGLISH_CATEGORY_MAPPINGS = {
    "(?i)^HC$": "Home Care",
    "(?i).*HOME.*CARE.*": "Home Care",
    "(?i).*HOUSEHOLD.*": "Home Care",
    "(?i).*LAUNDRY.*": "Home Care",
    "(?i)Cleaning.*agent.*": "Home Care",
    "(?i).*Detergent.*": "Home Care",

    "(?i)^OC$": "Oral Care",
    "(?i).*ORAL.*": "Oral Care",
    "(?i).*ORAL.*CARE.*": "Oral Care",
    "(?i).*Dental.*": "Oral Care",
    "(?i).*Dentifrices.*": "Oral Care",
    "(?i).*Mouthwash.*": "Oral Care",
    "(?i).*Toothpaste.*": "Oral Care",
    "(?i).*Toothbrush.*": "Oral Care",

    "(?i).*BABY.*CARE.*": "Personal Care",
    "(?i).*Mask.*": "Personal Care",
    "(?i).*SKIN.*CARE.*": "Personal Care",
    "(?i)Bath.*": "Personal Care",
    "(?i).*BEAUTY.*": "Personal Care",
    "(?i).*BODY.*CARE.*": "Personal Care",
    "(?i).*Conditioner.*": "Personal Care",
    "(?i).*Cosmetics.*": "Personal Care",
    "(?i).*CREMA.*PIEL.*": "Personal Care",
    "(?i).*Deodorant.*": "Personal Care",
    "(?i).*DEPILATOR.*": "Personal Care",
    "(?i).*DIAPER.*": "Personal Care",
    "(?i)Face.*Care.*": "Personal Care",
    "(?i).*Facial.*": "Personal Care",
    "(?i)Feminine.*Care.*": "Personal Care",
    "(?i).*Hair.*Care.*": "Personal Care",
    "(?i)Hair.*Colour.*": "Personal Care",
    "(?i)Hair.*Shampoo.*": "Personal Care",
    "(?i).*Hair.*Removal.*": "Personal Care",
    "(?i)Hair.*Styl.*": "Personal Care",
    "(?i)Hair.*Treatment.*": "Personal Care",
    "(?i)Hand.*Wash.*": "Personal Care",
    "(?i).*HIGIENE.*FEMENIN.*": "Personal Care",
    "(?i).*HYGIENE.*": "Personal Care",
    "(?i).*Moisturizer.*": "Personal Care",
    "(?i).*MOUTH.*CARE.*": "Personal Care",
    "(?i)^PC$": "Personal Care",
    "(?i).*PERSONAL.*CARE.*": "Personal Care",
    "(?i).*SOAP.*": "Personal Care",
    "(?i).*Shampoo.*": "Personal Care",
    "(?i).*SHAVE.*": "Personal Care",
    "(?i).*SHAVING.*": "Personal Care",
    "(?i)Shower.*": "Personal Care",
    "(?i).*Toiletries.*": "Personal Care",

    "(?i)Pet\\s.*": "Pet Nutrition",

    "(?i).*ANTISEPTIC.*": "Other",
    "(?i).*WHISKY.*": "Other",
    "(?i).*CHAMPAGNE.*": "Other",
    "(?i).*SHOW.*": "Other",
    "(?i).*SHOPPING.*": "Other",
    "(?i).*BOUTIQUE.*": "Other",
    "(?i).*KETCHUP.*": "Other",
    "(?i)(\b)?OTHER(\b)?": "Other",
    "(?i)(\b)?Others(\b)?": "Other",
    "(?i).*Accessories.*": "Other",
    "(?i).*Agriculture.*": "Other",
    "(?i).*Alcohol.*": "Other",
    "(?i)(\b)?ALL.*OTHER.*": "Other",
    "(?i).*Automation.*": "Other",
    "(?i).*Automotive.*": "Other",
    "(?i).*Banking.*": "Other",
    "(?i).*Beverage.*": "Other",
    "(?i).*Building.*": "Other",
    "(?i).*CEREAL.*": "Other",
    "(?i).*Cough.*": "Other",
    "(?i).*Clothing.*": "Other",
    "(?i).*Computers.*": "Other",
    "(?i).*Conglomerate.*": "Other",
    "(?i).*Corporate.*": "Other",
    "(?i).*Dairy.*": "Other",
    "(?i).*Drinks.*": "Other",
    "(?i).*Durables.*": "Other",
    "(?i).*Education.*": "Other",
    "(?i).*Equipments.*": "Other",
    "(?i).*Electrical.*": "Other",
    "(?i).*CONTAINER.*": "Other",
    "(?i).*TRAILER.*": "Other",
    "(?i).*Event.*": "Other",
    "(?i).*Finance.*": "Other",
    "(?i).*FOOD.*": "Other",
    "(?i).*Fuel.*": "Other",
    "(?i).*HARINA.*": "Other",
    "(?i).*HIGIENE.*PRODUCTO.*INFANTILE.*": "Other",
    "(?i).*HOTEL.*": "Other",
    "(?i).*COURIER.*": "Other",
    "(?i).*Internet.*": "Other",
    "(?i).*Investment.*": "Other",
    "(?i).*LACTEO.*": "Other",
    "(?i).*MEDIUM.*": "Other",
    "(?i).*PICK.*UP.*": "Other",
    "(?i).*MINI.*": "Other",
    "(?i).*PREMIUM.*": "Other",
    "(?i).*SMALL.*": "Other",
    "(?i).*UTILITY.*": "Other",
    "(?i).*Land.*": "Other",
    "(?i).*Materials.*": "Other",
    "(?i).*Medicated.*": "Other",
    "(?i).*Medicine.*": "Other",
    "(?i).*Miscellaneous.*": "Other",
    "(?i).*Muscle.*": "Other",
    "(?i).*Office.*": "Other",
    "(?i).*Petroleum.*": "Other",
    "(?i).*Pesticide.*": "Other",
    "(?i).*Pharmaceutical.*": "Other",
    "(?i).*Pharmacy.*": "Other",
    "(?i).*Retail.*": "Other",
    "(?i).*TEA.*": "Other",
    "(?i).*Telecom.*": "Other",
    "(?i).*Textil.*": "Other",
    "(?i).*Tobacco.*": "Other",
    "(?i).*Tourism.*": "Other",
    "(?i).*Transport.*": "Other",
    "(?i).*Vitamin.*": "Other",
}

SPANISH_CATEGORY_MAPPINGS = {
    "(?i).*INDEFINIDO.*": NOT_AVAILABLE,
    "(?i).*NO\sDISPONIBLE.*": NOT_AVAILABLE,

    "(?i).*BUCAL.*": "Oral Care",
    "(?i).*ANTISARR.*": "Oral Care",
    "(?i).*ANTISEPT.*BUC.*": "Oral Care",
    "(?i).*CEPILLO.*DENT.*": "Oral Care",

    "(?i).*DETERGENTE.*": "Home Care",
    "(?i).*REMOV.*MANCHA.*": "Home Care",
    "(?i).*PRODUCTO.*LIMPIEZA.*DOMESTICA.*": "Home Care",
    "(?i).*LIMP(I)?EZA.*": "Home Care",
    "(?i).*LIMP.*DOM.*": "Home Care",
    "(?i).*BLANQUEADOR.*": "Home Care",
    "(?i).*QUITAMANCHA.*": "Home Care",
    "(?i).*LIMPIADOR.*": "Home Care",
    "(?i).*PRODUCTO.*HOGAR.*": "Home Care",
    "(?i).*SUAVIZANTE.*": "Home Care",
    "(?i).*QUITAGRASA.*": "Home Care",
    "(?i).*ESCOBA.*": "Home Care",
    "(?i).*TOALLA.*PAPEL.*": "Home Care",
    "(?i).*PAPEL.*HIG(I)?ENIC(O)?.*": "Home Care",
    "(?i).*TOALLA.*ABSORB.*": "Home Care",
    "(?i).*HIGIENE.*HOGAR.*": "Home Care",
    "(?i).*LAVAPLATO.*": "Home Care",
    "(?i).*LAVALOZA.*": "Home Care",
    "(?i).*SERVILLETA.*": "Home Care",
    "(?i).*JABON.*BARRA.*": "Home Care",
    "(?i).*JABON.*LAVAR.*": "Home Care",
    "(?i).*DEODOR.*AMBIENT.*": "Home Care",
    "(?i).*DESINFEC.*": "Home Care",
    "(?i).*ARTICULO.*HOGAR.*": "Home Care",
    "(?i).*DESMANCHADOR.*": "Home Care",
    "(?i).*TRAPEADOR.*": "Home Care",

    "(?i).*COSMETICO.*": "Personal Care",
    "(?i).*MAQUIAGEM.*": "Personal Care",
    "(?i).*BELLEZA.*": "Personal Care",
    "(?i).*ESTRIA.*": "Personal Care",
    "(?i).*COSMETOLOG.*": "Personal Care",
    "(?i).*SHAMP.*": "Personal Care",
    "(?i).*TALCO.*": "Personal Care",
    "(?i).*CREM.*HIDRAT.*": "Personal Care",
    "(?i).*CREM.*ANTIARRU.*": "Personal Care",
    "(?i).*INTIM(O)?.*": "Personal Care",
    "(?i).*RINSE.*": "Personal Care",
    "(?i).*CHAMPU.*": "Personal Care",
    "(?i).*CREMA.*PIEL.*": "Personal Care",
    "(?i).*CREMA.*REGENERADOR.*": "Personal Care",
    "(?i).*MASCARILLA.*FAC.*": "Personal Care",
    "(?i).*HIG.*PERSONA.*": "Personal Care",
    "(?i).*TRATAMIENTO.*": "Personal Care",
    "(?i).*PROTECCION.*FEMENINA.*": "Personal Care",
    "(?i).*HIGIENE.*PRODUCTO.*INFANTIL.*": "Personal Care",
    "(?i).*FRAGANCIA.*": "Personal Care",
    "(?i).*FIJADOR.*CABELLO.*": "Personal Care",
    "(?i).*FIJADOR.*GEL.*": "Personal Care",
    "(?i).*PRODUCTO.*CABELLO.*": "Personal Care",
    "(?i).*DESODOR.*": "Personal Care",
    "(?i).*DESOD.*AERO.*": "Personal Care",
    "(?i).*CUTIS.*": "Personal Care",
    "(?i).*LABIAL.*": "Personal Care",
    "(?i).*ACNE.*": "Personal Care",
    "(?i).*PANALES.*": "Personal Care",
    "(?i).*PANALITIS.*": "Personal Care",
    "(?i).*PAÑALITIS.*": "Personal Care",
    "(?i).*PAÑAL.*": "Personal Care",
    "(?i).*TINT.*CABELLO.*": "Personal Care",
    "(?i).*CELULITI.*": "Personal Care",
    "(?i).*RASURADOR.*": "Personal Care",
    "(?i).*CREMA.*MANO.*": "Personal Care",
    "(?i).*CREM(A)?.*CUERPO.*": "Personal Care",
    "(?i).*CREMA.*PIERNA.*": "Personal Care",
    "(?i).*TRATAMIENTO.*CABELLO.*": "Personal Care",
    "(?i).*ANTIBACTERIAL.*": "Personal Care",
    "(?i).*CAPILAR.*": "Personal Care",
    "(?i).*COLAGENO.*": "Personal Care",
    "(?i).*JABON.*": "Personal Care",
    "(?i).*SABAO.*": "Personal Care",
    "(?i).*SABONETE.*": "Personal Care",
    "(?i).*MAQUILLAJE.*": "Personal Care",
    "(?i).*TOALLA.*MAQUILL.*": "Personal Care",
    "(?i).*TOALLA.*HIGIENICA.*": "Personal Care",
    "(?i).*TOALLA.*SANI.*": "Personal Care",
    "(?i).*CREMA.*MANCHA.*": "Personal Care",
    "(?i).*VARICE.*": "Personal Care",
    "(?i).*PERFUME.*": "Personal Care",
    "(?i).*FRAGRANCIA.*": "Personal Care",
    "(?i).*FRALDA.*": "Personal Care",
    "(?i).*TOALL.*HUM.*": "Personal Care",
    "(?i).*AFEIT.*": "Personal Care",
    "(?i).*PESTA(Ñ)?.*": "Personal Care",
    "(?i).*DRY.*CLEAN.*": "Personal Care",
    "(?i).*DENTIFRICO.*": "Personal Care",
    "(?i).*ANTIMICOTICO.*": "Personal Care",
    "(?i).*ACONDICIONAD.*": "Personal Care",
    "(?i).*TAMPON.*": "Personal Care",
    "(?i).*DELINEADOR.*": "Personal Care",
    "(?i).*BLOQUEADOR.*": "Personal Care",
    "(?i).*LOCION.*": "Personal Care",

    "(?i).*ALIMENTO.*PERRO.*": "Pet Nutrition",
    "(?i).*ALIMENTO.*MASCOT.*": "Pet Nutrition",

    "(?i).*COLEGIO.*": "Other",
    "(?i).*CONGRESO.*": "Other",
    "(?i).*MODA.*": "Other",
    "(?i).*EXPOSI.*": "Other",
    "(?i).*ORGANIZACI.*": "Other",
    "(?i).*PAIS.*": "Other",
    "(?i).*COCINA.*": "Other",
    "(?i).*VIVIENDA.*": "Other",
    "(?i).*PELUQUERIA.*": "Other",
    "(?i).*PAGINA.*": "Other",
    "(?i).*CAMARA.*": "Other",
    "(?i).*NOTARIA.*": "Other",
    "(?i).*INMOBILIARI.*": "Other",
    "(?i).*COOPERATIV.*": "Other",
    "(?i).*CDT.*": "Other",
    "(?i).*AUTOMOT.*": "Other",
    "(?i).*NUTRICION.*": "Other",
    "(?i).*(\b)?DISCO(\b)?.*": "Other",
    "(?i).*ADMINISTRATIV.*": "Other",
    "(?i).*OPTIC(O)?.*": "Other",
    "(?i).*AUTOSERVICIO.*": "Other",
    "(?i).*SERVIDOR.*": "Other",
    "(?i).*CREDITO.*": "Other",
    "(?i).*DEBITO.*": "Other",
    "(?i).*COMERCIO.*": "Other",
    "(?i).*GUBERNAMENTAL.*": "Other",
    "(?i).*DEPORTE.*": "Other",
    "(?i).*DIVERS.*": "Other",
    "(?i).*EMPRESA.*": "Other",
    "(?i).*EMPLEO.*": "Other",
    "(?i).*PROVEEDOR.*": "Other",
    "(?i).*BENEFIC(O)?.*": "Other",
    "(?i).*RESIDENCIA.*": "Other",
    "(?i).*HOTEL.*": "Other",
    "(?i).*INSECT.*": "Other",
    "(?i).*FUNGICIDA.*": "Other",
    "(?i).*SERVICIO.*": "Other",
    "(?i).*ALIMENTO.*": "Other",
    "(?i).*COMPUTACION.*": "Other",
    "(?i).*INSTITU.*": "Other",
    "(?i).*MOTOCICLETA.*": "Other",
    "(?i).*ROPA.*": "Other",
    "(?i).*SEGUR(O)?.*": "Other",
    "(?i).*TELEMERCADEO.*": "Other",
    "(?i).*TIENDA.*": "Other",
    "(?i).*EDUCACION.*": "Other",
    "(?i).*CULTURA.*": "Other",
    "(?i).*AGROPECUARI.*": "Other",
    "(?i).*COMPLEMENTO.*": "Other",
    "(?i).*CAJA.*COMPENSACION.*": "Other",
    "(?i).*CAJERO.*": "Other",
    "(?i).*COMPRA.*": "Other",
    "(?i).*PAUTA.*": "Other",
    "(?i).*VEHICULO.*": "Other",
    "(?i).*SOFTWARE.*": "Other",
    "(?i).*HARDWARE.*": "Other",
    "(?i).*MANTENIMIENTO.*": "Other",
    "(?i).*REPARACION.*": "Other",
    "(?i).*RESTAURANTE.*": "Other",
    "(?i).*GASOLIN.*": "Other",
    "(?i).*ASOCIACION.*": "Other",
    "(?i).*FINANCI.*": "Other",
    "(?i).*TELEVISION.*": "Other",
    "(?i).*UNIVERSI.*": "Other",
    "(?i).*PELICULA.*": "Other",
    "(?i).*PERIODICO.*": "Other",
    "(?i).*ESCUELA.*": "Other",
    "(?i).*INVERSION.*": "Other",
    "(?i).*VIAJE.*": "Other",
    "(?i).*BANC(O)?.*": "Other",
    "(?i).*RADIO.*": "Other",
    "(?i).*PROMOCION.*": "Other",
    "(?i).*AEREA.*": "Other",
    "(?i).*BOLSA.*": "Other",
    "(?i).*INDUSTRIA.*": "Other",
    "(?i).*COMUNIC.*": "Other",
    "(?i).*GIMNASIO.*": "Other",
    "(?i).*REVISTA.*": "Other",
    "(?i).*DOMEST.*": "Other",
    "(?i).*TEATRO.*": "Other",
    "(?i).*LIBRERIA.*": "Other",
    "(?i).*CURSO.*": "Other",
    "(?i).*PETROLE.*": "Other",
    "(?i).*CONFERENCIA.*": "Other",
    "(?i).*CINE.*": "Other",
    "(?i).*CONFECCION.*": "Other",
    "(?i).*DISTRIBUIDOR.*": "Other",
    "(?i).*PRIMA.*": "Other",
    "(?i).*COMPUTO.*": "Other",
    "(?i).*CRUCERO.*": "Other",
    "(?i).*TAXI.*": "Other",
    "(?i).*LAPTOP.*": "Other",
    "(?i).*MAPA.*": "Other",
    "(?i).*PORTAFOLIO.*": "Other",
    "(?i).*VOLTAJE.*": "Other",
    "(?i).*TELEFON.*": "Other",
    "(?i).*GALERIA.*": "Other",
    "(?i).*CONDOMINIO.*": "Other",
    "(?i).*DOMICILIO.*": "Other",
    "(?i).*AVION.*": "Other",
    "(?i).*ACADEMI.*": "Other",
    "(?i).*MULTIFUNCIONAL.*": "Other",
    "(?i).*FUNERA.*": "Other",
    "(?i).*LUBRICA.*": "Other",
    "(?i).*LUGAR.*": "Other",
    "(?i).*CASA.*CAMBIO.*": "Other",
    "(?i).*CASINO.*": "Other",
    "(?i).*CONSTRUC.*": "Other",
    "(?i).*HERRAMIENTA.*": "Other",
    "(?i).*CLINICA.*": "Other",
    "(?i).*CENTRO.*COMERCIAL.*": "Other",
    "(?i).*CENTRO.*NOCTURNO.*": "Other",
    "(?i).*LOTERIA.*": "Other",
    "(?i).*SALON.*": "Other",
    "(?i).*SALUD.*": "Other",
    "(?i).*OFICINA.*": "Other",
    "(?i).*MUSEO.*": "Other",
    "(?i).*ESTADIO.*": "Other",
    "(?i).*TUBERIA.*": "Other",
    "(?i).*ESPECTACULO.*": "Other",
    "(?i).*AGENCIA.*": "Other",
    "(?i).*ACCESORIO.*": "Other",
    "(?i).*GANADERIA.*": "Other",
    "(?i).*MINISTERIO.*": "Other",
    "(?i).*PAPELERIA.*": "Other",
    "(?i).*POLITIC.*": "Other",
    "(?i).*PENSION.*": "Other",
    "(?i).*PIROTECNICO.*": "Other",
    "(?i).*ALIANZA.*": "Other",
    "(?i).*POSTGRADO.*": "Other",
    "(?i).*SEGURIDAD.*": "Other",
    "(?i).*BIOENERGETIC.*": "Other",
    "(?i).*MUSIC.*": "Other",
    "(?i).*ALMACEN.*": "Other",
    "(?i).*CONVENCION.*": "Other",
    "(?i).*ANUNCIO.*": "Other",
    "(?i).*CAMPAÑA.*": "Other",
    "(?i).*LENCERIA.*": "Other",
    "(?i).*ASESOR.*": "Other",
    "(?i).*DECORA.*": "Other",
    "(?i).*MENSAJE.*": "Other",
    "(?i).*SONIDO.*": "Other",
    "(?i).*TALLER.*": "Other",
    "(?i).*FERIA.*": "Other",
    "(?i).*CLUB.*": "Other",
    "(?i).*FUNDACION.*": "Other",
    "(?i).*BICICLETA.*": "Other",
    "(?i).*APLICACION.*MOVIL.*": "Other",
    "(?i).*LEASING.*": "Other",
    "(?i).*CARNICERIA.*": "Other",
    "(?i).*ANTIGRIPAL.*": "Other",
    "(?i).*DESCONGESTION.*": "Other",
    "(?i).*INGENIER.*": "Other",
    "(?i).*REHABILITA.*": "Other",
    "(?i).*AHORRO.*": "Other",
    "(?i).*DROGUERIA.*": "Other",
    "(?i).*VETERINARI.*": "Other",
    "(?i).*RELIGIO.*": "Other",
    "(?i).*ANALGESICO.*": "Other",
    "(?i).*CLASIFICAD.*": "Other",
    "(?i).*MODIFICADOR.*": "Other",
    "(?i).*CARGA.*": "Other",
    "(?i).*FERTILIZANTE.*": "Other",
    "(?i).*PARQUE.*": "Other",
    "(?i).*ENDUL.*ANTE.*": "Other",
    "(?i).*SEMINARIO.*": "Other",
    "(?i).*GOBIERNO.*": "Other",
    "(?i).*COMBUSTIBLE.*": "Other",
    "(?i).*TURIST.*": "Other",
    "(?i).*AGRICOLA.*": "Other",
    "(?i).*BIEN.*RAI.*": "Other",
    "(?i).*MUNICIPAL.*": "Other",
    "(?i).*UNIFORME.*": "Other",
    "(?i).*MERCADO.*": "Other",
    "(?i).*REMESA.*": "Other",
    "(?i).*JUEGO.*": "Other",
    "(?i).*CUERO.*": "Other",
    "(?i).*IMPRESORA.*": "Other",
    "(?i).*PUBLICIDAD.*": "Other",
    "(?i).*INST.*PUBLIC.*": "Other",
    "(?i).*TRANSFERENCIA.*FONDO.*": "Other",
    "(?i).*CASA.*": "Other",
    "(?i).*HIGIENE.*ANIMAL.*": "Other",
    "(?i).*VENTA.*": "Other",
    "(?i).*MEDICAMENTO.*": "Other",
    "(?i).*MEDIO.*": "Other",
    "(?i).*DEPORTIVO.*": "Other",
    "(?i).*GUARDERIA.*": "Other",
    "(?i).*AVICOLA.*": "Other",
    "(?i).*DIGESTIVO.*": "Other",
    "(?i).*LABORATORIO.*": "Other",
    "(?i).*ANTICONCEPTIVO.*": "Other",
    "(?i).*CONCIERTO.*": "Other",
    "(?i).*ANTIHISTAMINICO.*": "Other",
    "(?i).*SASTRERIA.*": "Other",
    "(?i).*NASAL.*": "Other",
    "(?i).*EDITOR.*": "Other",
    "(?i).*ABOGAD.*": "Other",
    "(?i).*PREMIO.*": "Other",
    "(?i).*EMISORA.*": "Other",
    "(?i).*LABORATORIO.*": "Other",
    "(?i).*DEPORTIV.*": "Other",
    "(?i).*PROFESIONAL.*": "Other",
    "(?i).*FESTIVAL.*": "Other",
    "(?i).*IMPRENTA.*": "Other",
    "(?i).*COMPRESOR.*": "Other",
    "(?i).*CIRUJANO.*": "Other",
    "(?i).*CIRCO.*": "Other",
    "(?i).*MACROBIOTIC.*": "Other",
    "(?i).*CENTRO.*DROGA.*": "Other",
    "(?i).*CONSULTOR.*": "Other",
    "(?i).*CALCIO.*": "Other",
    "(?i).*QUIROPRACTICO.*": "Other",
    "(?i).*HOSPITAL.*": "Other",
    "(?i).*ADUANA.*": "Other",
    "(?i).*JOYERIA.*": "Other",
    "(?i).*AUTOMO.*": "Other",
    "(?i).*INFORME.*": "Other",
    "(?i).*INFORMATIC(A)?.*": "Other",
    "(?i).*CLIN.*MEDIC.*": "Other",
    "(?i).*FARMAC.*": "Other",
    "(?i).*ODONTOL.*": "Other",
    "(?i).*EQUIPO.*": "Other",
    "(?i).*GEL.*ANTIBACT.*": "Other",
    "(?i).*MAQUINA.*": "Other",
    "(?i).*QUIMIC.*": "Other",
    "(?i).*DIARIO.*": "Other",
    "(?i).*CELULAR.*": "Other",
    "(?i).*ZOOLOGICO.*": "Other",
    "(?i).*CARROCERIA.*": "Other",
    "(?i).*GUARDIA.*": "Other",
    "(?i).*TARJETA.*": "Other",
    "(?i).*GAS.*": "Other",
    "(?i).*NEUMATICO.*": "Other",
    "(?i).*LINEA.*INFANTIL.*": "Other",
    "(?i).*VESTUARIO.*": "Other",
    "(?i).*HERBICIDA.*": "Other",
    "(?i).*URBANIZACION.*": "Other",
    "(?i).*METAL.*": "Other",
    "(?i).*ENCICLOPEDIA.*": "Other",
    "(?i).*COORPORACION.*": "Other",
    "(?i).*SUPLEMENTO.*": "Other",
    "(?i).*EXCAVADOR.*": "Other",
    "(?i).*ESTACION.*": "Other",
}

CATEGORY_MAPPINGS = dict(SPANISH_CATEGORY_MAPPINGS, **ENGLISH_CATEGORY_MAPPINGS)

MONTH_REFERENCE_BY_LANGUAGE = {
     "ene": 1,
     "feb": 2,
     "mar": 3,
     "abr": 4,
     "may": 5,
     "jun": 6,
     "jul": 7,
     "ago": 8,
     "sep": 9,
     "oct": 10,
     "nov": 11,
     "dic": 12,
     
     "aug": 8,

     "jan" : 1,
     "fev": 2,
     "mai": 5,
     "set": 9,
     "out": 10,
     "dez": 12,

     "enero": 1,
     "febrero": 2,
     "marzo": 3,
     "abril": 4,
     "mayo": 5,
     "junio": 6,
     "julio": 7,
     "agosto": 8,
     "septiembre": 9,
     "octubre": 10,
     "noviembre": 11,
     "diciembre": 12,

     "september": 9,
     "october": 10,

     "setiembre": 9,
}
