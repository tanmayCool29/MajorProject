
import cv2
import pytesseract
import data_manipulation

def text_extraction_from_image(img):
    # image = cv2.imread('static/Almox-500-fake.jpg')
    # image = cv2.imread('static/med_1.png')
    image = cv2.imread(f'{img}')


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    results = pytesseract.image_to_data(gray_image, output_type=pytesseract.Output.DICT)


    ''' my work'''
    correct_words = []
    periodic_table = ['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'sodium', 'magnesium', 'aluminum', 'silicon', 'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc', 'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 'xenon', 'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 'livermorium', 'tennessine', 'oganesson']
    not_useful = ['-','dioxide','flavour', 'required','sucked', 'after', 'meals','uncoated', 'chewable', 'tablet', 'dried', 'aluminium', 'hydroxide', 'aluminium', 'silicate', 'hydrate', 'hydroxide', 'bhoir', 'indian', 'simethicone', 'erythrosine', 'ponceau', 'temperature', 'exceeding', 'abbott', 'medicines', 'verna', 'industrial', 'advised', 'advised', 'trademark', 'manufactured','tablets','syrup', 'each', 'hard', 'gelatin', 'capsule','mg', 'contains', ':', 'equivalent', 'excipients',  'colours', '&', 'used', 'in', 'empty', 'hard', 'gelatin', 'capsule', 'shell','store', 'protected', 'from', 'moisture', 'schedule', 'drug', 'warning', 'to', 'be', 'sold', 'by', 'retail', 'on','the', 'prescription', 'of', 'a', 'registered', 'medical', 'practitioner', 'only','&','capsule','dosage:', 'as', 'directed', 'by', 'the', 'physician','keep', 'medicine', 'out', 'reach', 'of', 'children', 'mfg', 'lic', 'no','made', 'in', 'india', 'by', ':','laboratories','at','himachal', 'pradesh','house','marg', '', 'lower', 'parel,', 'mumbai', '-', 'ip','the']
    for res in results['text']:
        res = res.lower()
        if (res not in not_useful) and (res.isalpha()) and ((len(res)>=5) and (res not in periodic_table)) and (res not in correct_words):
            correct_words.append(res)

    ''' my work'''

    # fake or not:
    fake = True
    my_vec = data_manipulation.vec

    for word in correct_words:
        if word in my_vec[word[0]]:
            print(f"found the word: {word}\n")
            print(my_vec[word[0]])
            fake=False

    return fake