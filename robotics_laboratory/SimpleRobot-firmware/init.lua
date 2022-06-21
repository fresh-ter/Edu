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


-- Control

function robot_forward( ... )
    print("Robot -> Forward")
end

function robot_stop( ... )
    print("Robot -> Stop")
end

function robot_turn_right( ... )
    print("Robot -> Right")
end

function robot_turn_left( ... )
    print("Robot -> Left")
end

function robot_back( ... )
    print("Robot -> Back")
end

-- Server

require("httpserver").createServer(80, function(req, res)
    if req.url == "/forward" then
        robot_stop()
        robot_forward()

    elseif req.url == "/stop" then
        robot_stop()

    elseif req.url == "/right" then
        robot_turn_right()

    elseif req.url == "/left" then
        robot_turn_left()
        
    elseif req.url == "/back" then
        robot_stop()
        robot_back()
    end

    res:finish("Hello, world!")
end)
