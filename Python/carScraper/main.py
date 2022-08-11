import requests
from currency_converter import CurrencyConverter
from bs4 import BeautifulSoup
import sqlite3
import xlsxwriter

list_of_cars = []  # init. empty list for all the cars, placeholder for a database
car_links = []

class Car:  # create car object
    def __init__(self, brand=None, price=None, link=None, model=None, year=None, kms=None, fuel=None, engine_capacity=None, power=None,
                 body_type=None, doors=None, transmission=None, emissions=None, country_of_origin=None, color=None,
                 quality=None, number_of_spaces=None, negotiable_price=False, inmatriculat=False, primul_proprietar=False,
                 timbru_de_mediu_platit=False, fara_accident=False, avariat=False, pentru_dezmembrare=False,
                 volan_pe_dreapta=False, predare_leasing=False, disponibil_de_inchiriat=False,
                 pt_pers_cu_dizabilitati=False, accept_schimb=False):  # TODO rename romanian stuff to english
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
        self.number_of_spaces = number_of_spaces
        self.negotiable_price = negotiable_price
        self.inmatriculat = inmatriculat
        self.primul_proprietar = primul_proprietar
        self.timbru_de_mediu_platit = timbru_de_mediu_platit
        self.fara_accident = fara_accident
        self.avariat = avariat
        self.pentru_dezmembrare = pentru_dezmembrare
        self.volan_pe_dreapta = volan_pe_dreapta
        self.predare_leasing = predare_leasing
        self.disponibil_de_inchiriat = disponibil_de_inchiriat
        self.pt_pers_cu_dizabilitati = pt_pers_cu_dizabilitati
        self.accept_schimb = accept_schimb


def get_more_pages(URL):  # only tested with alfa so far, but it worky worky
    page_links = []
    page_links.append(URL)
    can_find_pages = True
    while can_find_pages:
        try:
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find("li", class_="next_page")
            results2 = results.find("a", class_="rounded")
            newest_page = results2.get('href')
            page_links.append(newest_page)
            URL = newest_page
        except:
            print("No more pages for given brand")
            can_find_pages = False
    print("before delete: ", page_links)
    if page_links[-1] == "javascript:void(0)":
        del page_links[-1]
    print("after delete: ", page_links)
    return page_links


def keyword_correction(keyword):  # TODO do it for more brands
    keyword = keyword.lower()
    word_to_change = ["alfaromeo", "alfa romeo"]
    if keyword in word_to_change:
        keyword = "alfa-romeo"
    return keyword


def print_all_attributes(car):
    print(f"Brand: {car.brand} \nPrice: {car.price} \nModel: {car.model} \nYear: {car.year} \nKms: {car.kms} \n"
          f"Fuel: {car.fuel} \nEngine Capacity: {car.engine_capacity} \nPower: {car.power} \n"
          f"Body type: {car.body_type} \nNumber of doors: {car.doors} \nTransmission: {car.transmission} \n"
          f"Emissions: {car.emissions} \nCountry of origin: {car.country_of_origin} \nColor: {car.color} \n"
          f"Quality: {car.quality}\nLink: {car.link}\n ---------- \n")


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
    print("URL:", URL)

    def get_brand():
        return (entry.find("a")).text

    def set_brand(data):  # rewrite getters to setters
        car.brand = data

    def get_model():
        return (entry.find("a")).text

    def set_model(data):
        car.model = data

    def get_year():
        return (entry.find("a")).text

    def set_year(data):
        car.year = data

    def get_kms(kms):
        kms = "".join(kms.split())
        kms = kms.replace("Rulaj", "")
        kms = kms.replace("Verificăkm!", "")
        return kms

    def get_body_type():
        return (entry.find("a")).text

    def set_body_type(data):
        car.body_type = data

    def get_fuel():
        return (entry.find("a")).text

    def set_fuel(data):
        car.fuel = data

    def get_quality():
        return (entry.find("a")).text

    def set_quality(data):
        car.quality = data

    def get_engine_capacity():
        return (entry.find("a")).text

    def set_engine_capacity(data):
        car.engine_capacity = data

    def get_power():
        return (entry.find("a")).text

    def set_power(data):
        car.power = data

    def get_transmission():
        return (entry.find("a")).text

    def set_transmission(data):
        car.transmission = data

    def get_number_of_spaces():
        return (entry.find("a")).text

    def set_number_of_spaces(data):
        car.number_of_spaces = data

    def get_doors():
        return (entry.find("a")).text

    def set_doors(data):
        car.doors = data

    def get_negotiable():
        return True

    def set_negotiable(data):
        car.negotiable_price = True

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


    car = Car()

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    primary_results = soup.find("div", id="extra-fields")
    results = primary_results.findAll("div", {'class': ['filter_margin', '']})

    price = soup.find("span", id="price")
    price = price.text
    car.price = get_price(price)  # get price separately because it's stored elsewhere

    car.link = URL

    results = soup.find("div", id="extra-fields")
    results2 = results.findAll("div", class_="filter_margin")
    kms = results2[3].text
    car.kms = get_kms(kms)

    for entry in results:  # should work with a dictionary now
        try:
            # TODO redo this into a def, trimming span
            span = entry.find("span")
            span = span.text
            span = "".join(span.split())
            span = span.lower()
            #print("span: ", span)
            data = entry.find("a").text
            # just suck it up and do the ungodly if else, fix it later, you just should just focus on getting something working as of now
            if span == "marcă":  # change to dictionary later and figure out how to add parts into car obj
                set_brand(data)
                #print("brand: ", brand)
            elif span == "model":
                set_model(data)
                #print("model: ", model)
            elif span == "caroserie":
                set_body_type(data)
                #print("model: ", body_type)
            elif span == "anfabricație":
                set_year(data)
            elif span == "combustibil":
                set_fuel(data)
            elif span == "stare":
                set_quality(data)
            elif span == "capacitatemotor":
                set_engine_capacity(data)
            elif span == "putere":
                set_power(data)
            elif span == "cutiedeviteze":
                set_transmission(data)
            elif span == "numărdelocuri":
                set_number_of_spaces(data)
            elif span == "număruşi":
                set_doors(data)
            elif span == "prețnegociabil":
                set_negotiable(data)
        except:
            pass
    list_of_cars.append(car)

def write_to_excel():
    row = 1
    column = 0
    workbook = xlsxwriter.Workbook('F:/Projects/Python/carScraper/car_data.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "brand")
    worksheet.set_column('A:A', 20)
    worksheet.write(0, 1, "model")
    worksheet.write(0, 2, "price")
    worksheet.write(0, 3, "mileage")
    worksheet.write(0, 4, "year")
    worksheet.write(0, 5, "fuel")
    for car in list_of_cars:
        brand = car.brand
        model = car.model
        price = car.price
        kms = car.kms
        year = car.year
        fuel = car.fuel
        worksheet.write(row, column, brand)
        worksheet.write(row, column+1, model)
        worksheet.write(row, column+2, price)
        worksheet.write(row, column+3, kms)
        worksheet.write(row, column + 4, year)
        worksheet.write(row, column + 5, fuel)
        row += 1
    workbook.close()
test_mode = False
if not test_mode:
    if input("Do you want to search all brands? (Warning, will take a lot of time) Y/N") == "Y":
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
        brands_to_search = ["skoda"]  #, "volvo", "skoda"]  # it keeps going back to mercedes for some reason after finishing it, figure out why
    for brand in brands_to_search:
        try:
            URL = search(brand)  # search for given brand TODO add models too
            asd123 = get_more_pages(URL)
            for index in range(len(asd123)):  # code to get the second and subsequent pages
                URL = asd123[index]
                print("URL: ", URL)
                print(len(asd123))
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find(id="list_cart_holder")
                try:
                    individual_results = results.findAll("a")
                    print("Cars found in: brand: ", brand, " Url: ", URL)
                    for result in individual_results:
                        car_links.append(result.get('href'))  # get all links
                except:
                    print("No cars found in: brand: ", brand, " Url: ", URL)
                    pass
            for link in car_links:
                get_car_data(link)
        except:
            pass
    #for car in list_of_cars:
        #print_all_attributes(car)
else:
    get_car_data("https://carzz.ro/alfa-romeo-giulietta-anunt_3132877.html")
    for car in list_of_cars:
        print_all_attributes(car)

print("writing to excel")
write_to_excel()
print ("written to excel")