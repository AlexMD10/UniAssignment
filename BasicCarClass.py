class Car:
    MIN_NUM_OF_SEATS = 1
    MAX_NUM_OF_SEATS = 10
    MAX_WIDTH = 2500
    MIN_WIDTH = 1000
    MAX_LENGTH = 10000
    MIN_LENGTH = 1000
    MAX_MPG = 80
    MIN_MGP = 5
    MAX_MAX_SPEED = 310
    MIN_MAX_SPEED = 30

    def __init__(self, car_id, reg_num, manufacturer, model_type, sipp_code, max_seating_capacity, car_width, car_length, max_speed, mpg, on_hire):

        self.car_ID = car_id
        self.Reg_Num = reg_num
        self.Manufacturer = manufacturer
        self.Model_Type = model_type
        self.Sipp_Code = sipp_code
        self.Max_Seating_Capacity = max_seating_capacity
        self.Width = car_width
        self.Length = car_length
        self.Max_Speed = max_speed
        self.Mpg = mpg
        self.On_Hire = on_hire

    def __str__(self):
        return f"{self.car_ID} {self.reg_num} {self.manufacturer} {self.model_type} {self.sipp_code} {self.max_seating_capacity} {self.width} {self.length} {self.max_speed} {self.mpg} {self.on_hire}"

   # @property
    def reg_num(self):
       return self.reg_num

    #@reg_num.setter
    def reg_num(self, reg_num):
        self.reg_num = reg_num

    # @property
    def manufacturer(self):
        return self.manufacturer

    #@manufacturer.setter
    def manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    # @property
    def model_type(self):
        return self.model_type

#    @model_type.setter
    def model_type(self, model):
        self._model_type = model

    # @property
    def sipp_code(self):
        return self.sipp_code

#    @sipp_code.setter
    def sipp_code(self, sipp_code):
        self._sipp_code = sipp_code

    # @property
    def max_seating_capacity(self):
        return self.max_seating_capacity

    #@max_seating_capacity.setter
    def max_seating_capacity(self, seat_capacity: int):
        if Car.MIN_NUM_OF_SEATS <= seat_capacity <= Car.MAX_NUM_OF_SEATS:
            self._max_seating_capacity = seat_capacity
        else:
            self._max_seating_capacity = 0
            print('Invalid number of seats')

    # @property
    def width(self):
        return self.width

   # @width.setter
    def width(self, width: int):
        if Car.MIN_WIDTH <= width <= Car.MAX_WIDTH:
            self._car_width = width
        else:
            self._car_width = 0
        print('Width has to be between 1000 and 2500')

    # @property
    def length(self):
        return self.length

#    @length.setter
    def length(self, length):
        if Car.MIN_LENGTH <= length <= Car.MAX_LENGTH:
            self._length = length
        else:
            self._length = 0
        print('Length has to be between 1000 and 10000')

    # @property
    def max_speed(self):
        return self.max_speed

#    @max_speed.setter
    def max_speed(self, max_speed):
        if Car.MIN_MAX_SPEED <= max_speed <= Car.MAX_MAX_SPEED:
            self._max_speed = max_speed
        else:
            self._max_speed = 0
        print('Max Speed has to be between 30 and 310mph')

    # @property
    def mpg(self):
        return self.mpg

#    @mpg.setter
    def mpg(self, mpg):
        if Car.MIN_MGP <= mpg <= Car.MAX_MPG:
            self._mpg = mpg
        else:
            self._mpg = 0
        print('Mpg has to be between 5 and 80')

    def on_hire(self):
        return self.on_hire

    def on_hire(self, on_hire):
        self._on_hire = on_hire

