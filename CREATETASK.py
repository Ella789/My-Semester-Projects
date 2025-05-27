#---Pie making---
while True:
    pie_types = ["ApplePie","PumpkinPie","FrenchSilkPie","CherryPie","BananaCreamPie","KeyLimePie","PecanPie","CoconutCreamPie","BlueberryPie","LemonMeringuePie","SweetPotatoPie", "PeachPie", "CranberryPie","CookiesandCreamPie"]
    pie_mainingrediant = ["Apple, pie crust, sugar, flour, butter, and spices","Pumpkin, pie crust, sugar, eggs, evaporated milk, and spices","Chocolate, pie crust, eggs, sugar, butter, heavy cream","cherries, pie crust, sugar, cornstarch,","pie crust, vanilla custard filling, sliced bananas","pie crust, sweetened condensed milk, lime juice and zest, and egg yolks,","eggs, butter, sugar, corn syrup, vanilla, pecans","milk, sugar, egg yolks, cornstarch, coconut milk","blueberries, sugar, all-purpose flour, butter, pie crust","pie crust, lemon juice, lemon zest, eggs, sugar,butter","sweet potatoes, sugar, eggs, butter, evaporated milk, all-purpose flour, vanilla extract, spices, pie crust","peaches, sugar, all-purpose flour, butter, lemon juice, spices, pie crust","cranberries, sugar, flour, pie crust","pie crust, strawberries, rhubarb, sugar, flour"," Oreo cookies, butter, cream cheese, heavy cream, sour cream, powdered sugar, vanilla extract"]
    pie_images = ["https://www.recipetineats.com/tachyon/2022/11/Apple-Pie_8.jpg","https://tinyurl.com/4a7wbwuk","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwrHy6Ge3jE2DEc45SgUfv6UdzZIS5XYmEUA&s","https://joyfoodsunshine.com/wp-content/uploads/2022/05/sweet-cherry-pie-recipe-9.jpg","https://tastesbetterfromscratch.com/wp-content/uploads/2023/11/Banana-Cream-Pie-1.jpg","https://tinyurl.com/mt6dynp2","https://patijinich.com/wp-content/uploads/2018/08/Ep-713-Dulce-de-Leche-Caramel-Chocolate-Pecan-Pie.jpg","https://tinyurl.com/yhm7hck2","https://tastesbetterfromscratch.com/wp-content/uploads/2023/11/Blueberry-Pie-1.jpg","https://carlsbadcravings.com/wp-content/uploads/2023/04/Lemon-Meringue-Pie-11.jpg","https://www.daringgourmet.com/wp-content/uploads/2020/11/Sweet-Potato-Pie-Recipe-2.jpg","https://damnspicy.com/wp-content/uploads/2023/07/peach-pie-with-fresh-peaches-recipe-683x1024.jpg","https://www.chsugar.com/sites/default/files/2023-11/Web_Hero_Image-Cranberry%20Pie%207%20%282%29%20%281%29_0.jpg","https://sallysbakingaddiction.com/wp-content/uploads/2020/10/cookies-and-cream-pie.jpg"]
    pie_time = ["45","45","20","60","25","20","75","30","70","20","45","60","45","5"]
    diffuculty_list=["hard","hard","easy","hard","easy","medium","hard","hard","medium","medium","hard","medium","easy","hard","easy"]
    filtered_list=[]
    from PIL import Image
    import requests
    from io import BytesIO
    def open_image(url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
    def pie():
        x = input("What pie are you planning to bake?")
        for i in range(len(pie_types)):
            if x in pie_types[i]:
                open_image(pie_images[i])
    def time():
        x = input("Input a bake time and I will recommend you pies that fit your time")
        for i in range(len(pie_time)):
            if x in pie_time[i]:
                print(pie_types[i])
    def grocery(level):
        if level == "hard":
            for i in range(len(pie_mainingrediant)):
                if diffuculty_list[i]=="hard":
                    filtered_list.append(pie_mainingrediant[i])
                    print(filtered_list)
        if level == "easy":
            for i in range(len(pie_mainingrediant)):
                if diffuculty_list[i]=="easy":
                    filtered_list.append(pie_mainingrediant[i])
                    print(filtered_list)
        if level == "medium":
            for i in range(len(pie_mainingrediant)):
                if diffuculty_list[i]=="medium":
                    filtered_list.append(pie_mainingrediant[i])
                    print(filtered_list)
    def abc(letter):
        for s in pie_types:
            if s.startswith(letter):
                print(s)
    def pie_maker():
        pie()
        time()
        grocery("easy")
        letter = input("type a letter and i'll search the list for a pie that starts with the letter")
        abc(letter)
    #Main
    pie_maker()
    break
