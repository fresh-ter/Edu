-- start delay
tmr.delay(5000000)

-- config

wifi.setmode(wifi.SOFTAP)
station_cfg={}
station_cfg.ssid="SimpleRobot"
station_cfg.pwd="robotpass"
station_cfg.save=false
wifi.ap.config(station_cfg)
cfg =
{
    ip="192.168.1.1",
    netmask="255.255.255.0",
    gateway="192.168.1.1"
}
wifi.ap.setip(cfg)

print("Hello, world!")


-- Pin control

-- 1 - left forward
-- 2 - left back
-- 3 - right forward
-- 4 - right back

gpio.mode(1, gpio.OUTPUT)
gpio.mode(2, gpio.OUTPUT)
gpio.mode(3, gpio.OUTPUT)
gpio.mode(4, gpio.OUTPUT)


-- Control

function robot_forward( ... )
    print("Robot -> Forward")
    gpio.write(1, gpio.HIGH)
    gpio.write(3, gpio.HIGH)
end

function robot_stop( ... )
    print("Robot -> Stop")
    gpio.write(1, gpio.LOW)
    gpio.write(2, gpio.LOW)
    gpio.write(3, gpio.LOW)
    gpio.write(4, gpio.LOW)
end

function robot_turn_right( ... )
    print("Robot -> Right")
    gpio.write(1, gpio.HIGH)
end

function robot_turn_left( ... )
    print("Robot -> Left")
    gpio.write(3, gpio.HIGH)
end

function robot_back( ... )
    print("Robot -> Back")
    gpio.write(2, gpio.HIGH)
    gpio.write(4, gpio.HIGH)
end

-- Server

require("httpserver").createServer(80, function(req, res)
    if req.url == "/forward" then
        robot_stop()
        robot_forward()

    elseif req.url == "/stop" then
        robot_stop()

    elseif req.url == "/right" then
        robot_stop()
        robot_turn_right()

    elseif req.url == "/left" then
        robot_stop()
        robot_turn_left()
        
    elseif req.url == "/back" then
        robot_stop()
        robot_back()
    end

    res:finish("Hello, world!")
end)
