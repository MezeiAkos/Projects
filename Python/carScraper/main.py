import requests
from halo import Halo
from currency_converter import CurrencyConverter
from bs4 import BeautifulSoup

spinner = Halo(text='Loading', spinner='dots')  # initialize spinner so I know if my program froze
list_of_cars = []  # make global list for all the cars


# get brand without whitespace and other text
def get_brand(brand):
    brand = "".join(brand.split())  # remove all whitespace
    brand = brand.replace("Marcă", "")  # get rid of extra text
    return brand


def get_model(model):
    model = "".join(model.split())
    model = model.replace("Model", "")
    return model


def get_year(year):
    year = "".join(year.split())
    year = year.replace("Anfabricație", "")
    return year


def get_kms(kms):
    kms = "".join(kms.split())
    kms = kms.replace("Rulaj", "")
    kms = kms.replace("Verificăkm!", "")
    return kms


def get_price(price):
    price = "".join(price.split())
    price = price.replace("eur", "")
    price = price.replace(".", "")
    if "lei" in price:  # if price is in lei, convert to eur
        c = CurrencyConverter()
        price = price.replace("lei", "")
        price = int(price)
        price = c.convert(price, 'RON', 'EUR')
    return int(price)  # return price as integer


class Car:  # create car object
    def __init__(self, brand, price, link, model=None, year=None, kms=None, fuel=None, engine_capacity=None, power=None,
                 body_type=None, doors=None, transmission=None, emissions=None, country_of_origin=None, color=None,
                 quality=None):  # TODO all the checkmark things too
        self.brand = brand
        self.price = price
        self.link = link
        self.model = model
        self.year = year
        self.kms = kms
        self.fuel = fuel
        self.engine_capacity = engine_capacity
        self.power = power
        self.body_type = body_type
        self.doors = doors
        self.transmission = transmission
        self.emissions = emissions
        self.country_of_origin = country_of_origin
        self.color = color
        self.quality = quality


def keyword_correction(keyword):  # TODO do it for more brands
    keyword = keyword.lower()
    word_to_change = ["alfaromeo", "alfa romeo"]
    if keyword in word_to_change:
        keyword = "alfa-romeo"
    return keyword


def search(keyword):  # check if searched brand results in useable html page
    # TODO do brand name correction, ex: alfaromeo -> alfa-romeo
    brands = ['abarth', 'acura', 'aixam', 'alfa-romeo', 'alta', 'aro', 'astonmartin', 'audi', 'austin', 'bentley',
              'bmw', 'brilliance', 'bugatti', 'buick', 'cadillac', 'caterham', 'chery', 'chevrolet', 'chrysler',
              'citroen', 'comarth', 'dacia', 'daewoo', 'daihatsu', 'delorean', 'dkw', 'dodge', 'eagle', 'ferrari',
              'fiat', 'ford', 'galloper', 'gaz', 'geely', 'gmc', 'gordon', 'grecav', 'gwm', 'holden', 'honda', 'hummer',
              'hyundai', 'infiniti', 'innocenti', 'isuzu', 'jaguar', 'jeep', 'kaipan', 'kia', 'lada', 'lamborghini',
              'lancia', 'landrover', 'lexus', 'lincoln', 'lotus', 'lti', 'mahindra', 'marcos', 'maruti', 'maserati',
              'maybach', 'mazda', 'mercedes-benz', 'mercury', 'mg', 'microcar', 'mini', 'mitsubishi', 'morgan',
              'moskwicz', 'nissan', 'nsu', 'nysa', 'oldsmobile', 'oltcit', 'opel', 'peugeot', 'plymouth', 'polonez',
              'pontiac', 'porsche', 'proton', 'raytonfissore', 'renault', 'rolls-royce', 'rover', 'saab', 'santana',
              'scion', 'seat', 'shuanghuan', 'skoda', 'skywell', 'smart', 'ssangyong', 'staurn', 'subaru', 'suda',
              'suzuki', 'syrena', 'talbot', 'tarpan', 'tata', 'tatra', 'tavria', 'tesla', 'toyota', 'trabant',
              'triumph', 'tvr', 'uaz', 'vauxhall', 'volga', 'volkswagen', 'volvo', 'warszawa', 'wartburg', 'yugo',
              'zaporozec', 'zastawa', 'zuk']

    if keyword in brands:
        URL = "https://carzz.ro/autoturisme-" + keyword.lower() + ".html"
        return URL
    else:
        print("keyword not valid")


def get_car_data(URL):

    #spinner.start()  # start spinner
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", id="extra-fields")
    results2 = results.findAll("div", class_="filter_margin")
    # h2 -> brand, h3 -> model, h4 -> None, h5 -> year, h6 -> kms
    # TODO combustibil and caroserie has no class, figure out how to get that shit too somehow
    brand = results2[0].text
    brand = get_brand(brand)
    # print("brand: ", brand)
    model = results2[1].text
    model = get_model(model)
    # print("model: ", model)
    year = results2[2].text
    year = get_year(year)
    # print("year: ", year)
    kms = results2[3].text
    kms = get_kms(kms)
    # print("kms: ", kms)
    # seems like results2[0] is brand, [1] is model etc
    price = soup.find("span", id="price")
    price = price.text
    price = get_price(price)
    # print("price: ", price)
    # print("------------------")
    if price > 100:  # filter out cars for not really for sale, for parts, swaps etc based on low price
        list_of_cars.append(Car(brand, price, URL, model, year, kms))  # create car object and add to list
        print(len(list_of_cars))

#spinner.stop()  # stop spinner

car_links = []
f = open("listOfCars.txt", "w")
if input("Do you want to search all brands? (Warning, will take a lot of time) Y/N" ) == "Y":
    brands_to_search = [
        'abarth', 'acura', 'aixam', 'alfa-romeo', 'alta', 'aro', 'astonmartin', 'audi', 'austin', 'bentley',
        'bmw', 'brilliance', 'bugatti', 'buick', 'cadillac', 'caterham', 'chery', 'chevrolet', 'chrysler',
        'citroen', 'comarth', 'dacia', 'daewoo', 'daihatsu', 'delorean', 'dkw', 'dodge', 'eagle', 'ferrari',
        'fiat', 'ford', 'galloper', 'gaz', 'geely', 'gmc', 'gordon', 'grecav', 'gwm', 'holden', 'honda', 'hummer',
        'hyundai', 'infiniti', 'innocenti', 'isuzu', 'jaguar', 'jeep', 'kaipan', 'kia', 'lada', 'lamborghini',
        'lancia', 'landrover', 'lexus', 'lincoln', 'lotus', 'lti', 'mahindra', 'marcos', 'maruti', 'maserati',
        'maybach', 'mazda', 'mercedes-benz', 'mercury', 'mg', 'microcar', 'mini', 'mitsubishi', 'morgan',
        'moskwicz', 'nissan', 'nsu', 'nysa', 'oldsmobile', 'oltcit', 'opel', 'peugeot', 'plymouth', 'polonez',
        'pontiac', 'porsche', 'proton', 'raytonfissore', 'renault', 'rolls-royce', 'rover', 'saab', 'santana',
        'scion', 'seat', 'shuanghuan', 'skoda', 'skywell', 'smart', 'ssangyong', 'staurn', 'subaru', 'suda',
        'suzuki', 'syrena', 'talbot', 'tarpan', 'tata', 'tatra', 'tavria', 'tesla', 'toyota', 'trabant',
        'triumph', 'tvr', 'uaz', 'vauxhall', 'volga', 'volkswagen', 'volvo', 'warszawa', 'wartburg', 'yugo',
        'zaporozec', 'zastawa', 'zuk']
else:
    brands_to_search = ["alfa-romeo"]
for brand in brands_to_search:
    URL = search(brand)  # search for given brand TODO add models too
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="list_cart_holder")
    try:
        individual_results = results.findAll("a")
        print("Cars found in: brand: ",brand," Url: ", URL)
        for result in individual_results:
            car_links.append(result.get('href'))  # get all links
        for link in car_links:
            get_car_data(link)
    except:
        print("No cars found in: brand: ", brand, " Url: ", URL)
        pass
    f.write(brand)
    f.write("\n \n")
    for car in list_of_cars:
        print("Brand: ", car.brand, " Model: ", car.model, " Price: ", car.price)
        f.write(f"Model: {car.model}    Price: {car.price}  Year: {car.year}   Kms: {car.kms}   Url: {car.link}")
        f.write("\n ")
    list_of_cars.clear()
f.close()
# TODO make it look at all pages, not just the first
