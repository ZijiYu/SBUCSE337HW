module Towable
  def can_tow?(pounds)
    pounds < 2000
  end
end

class Vehicle
  @@number_of_vehicle = int(0.0)

  def initialize(year, modle, color)
    @year = year
    @modle = modle
    @color = color
    @@number_of_vehicle +=1
    @current_speed = 0
  end

  def self.number_of_doors
    puts "This program has created #{@@number_of_vehicles} vehicles"
  end

  def speed_up(number)
    @current_speed += number
    puts "You push the gas and accelerate #{number} mph."
  end

  def brake(number)
    if @current_speed >= number
      @current_speed -= number
      puts "You push the brake and decelerate #{number} mph."
    else
      puts "You push the brake and decelerate #{0} mph."
    end


  end

  def current_speed
    puts "You are now going #{@current_speed} mph"
  end

  def shut_down
    @current_speed = 0
    puts "Let's park the car!"
  end

  def spray_paint(color)
    self.color = color
    puts "Your new #{color} paint job looks great"
  end

  protected

  attr_accessor :color
end



# subclass

class MyCar < Vehicle
  NUMER_OF_DOORS = 4
  include Towable
  def to_s()
    "My car is a #{@color}, #{@year} ,#{@modle} !"
  end
  def self.gas_mileage(gallons, miles)
    puts "#{miles/gallons} miles per gallon of gas"
  end
end

class MyTruck < Vehicle
  NUMER_OF_DOORS = 2
  include Towable
  def to_s()
    "My truck is a #{@color}, #{@year} ,#{@modle} !"
  end
end




puts lumina = MyCar.new(1997, 'chevy lumina', 'white')
puts lumina.speed_up(20)
puts lumina.current_speed
puts lumina.speed_up(20)
puts lumina.current_speed
puts lumina.to_s
puts lumina.brake(20)
puts lumina.current_speed
puts lumina.brake(20)
puts lumina.current_speed
puts lumina.shut_down
puts MyCar.gas_mileage(13, 351)
puts lumina.spray_paint("red")
puts ram = MyTruck.new(1990, 'GMC', "black")
puts ram.can_tow?(1000)
puts lumina.can_tow?(3000)