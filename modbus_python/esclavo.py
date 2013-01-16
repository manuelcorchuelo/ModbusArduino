#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import sys

#add logging capability
import logging
import threading

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_rtu as modbus_rtu
import serial
import time

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
    
if __name__ == "__main__":
    #creamos el servidor indicandole el puerto y la velocidad en baudios
    server = modbus_rtu.RtuServer(serial.Serial(port="/dev/ttyACM0",baudrate=9600)) 

        
    try:
        logger.info("running...")
        
        server.start()
        
        # añadimos un esclavo
        slave_1 = server.add_slave(1) 
        slave_1.add_block('0', cst.HOLDING_REGISTERS, 100, 3)
        while True:
            # igualamos a dato el valor que leemos del esclavo, 3 registros a partir del registro 100
            time.sleep(0.10)
            dato = slave_1.get_values("0",100,3) 
            print dato[0],dato[1],dato[2]
    finally:
        server.stop()
