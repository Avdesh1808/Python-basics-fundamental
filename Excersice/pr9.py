class car:
    brand_name = "honda"
    model = 'city safari'
    model_no = 1200
    
    def details(self):
        print(f"{self.brand_name},{self.model},{self.model_no}")
a = car()
a.brand_name = "bmw"
a.model = "supreme"
a.model_no = 3200

a.details()

