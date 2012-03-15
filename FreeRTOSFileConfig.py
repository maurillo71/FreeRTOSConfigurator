#!/usr/bin/env python
# encoding: utf-8
#
# Copyright 2012 Mauro Gamba <maurillo71@gmail.com>
#
#
# Author: Mauro Gamba <maurillo71@gmail.com>
#

import os
import re

class FreeRTOSFileConfig:
    def __init__(self, fileName):
        # Create list of recognized parameters
        self.freeRTOSParametersName = [ \
    'configUSE_PREEMPTION',  'configUSE_IDLE_HOOK', 'configUSE_TICK_HOOK', \
    'configCPU_CLOCK_HZ',  'configTICK_RATE_HZ',  'configMAX_PRIORITIES',  \
    'configMINIMAL_STACK_SIZE',  'configTOTAL_HEAP_SIZE',  'configMAX_TASK_NAME_LEN', \
    'configUSE_TRACE_FACILITY',  'configUSE_16_BIT_TICKS',  'configIDLE_SHOULD_YIELD',  \
    'configUSE_MUTEXES',  'configUSE_RECURSIVE_MUTEXES',  'configUSE_COUNTING_SEMAPHORES',  \
    'configUSE_ALTERNATIVE_API',  'configCHECK_FOR_STACK_OVERFLOW',  'configQUEUE_REGISTRY_SIZE',  \
    'configGENERATE_RUN_TIME_STATS',  'configUSE_CO_ROUTINES',  'configMAX_CO_ROUTINE_PRIORITIES',  \
    'configUSE_TIMERS',  'configTIMER_TASK_PRIORITY',  'configTIMER_QUEUE_LENGTH',  \
    'configTIMER_TASK_STACK_DEPTH',  'configKERNEL_INTERRUPT_PRIORITY',  'configMAX_SYSCALL_INTERRUPT_PRIORITY',  \
    'configASSERT']
        
        # Create the useful regexp
        self.parameterDefinition = re.compile(r"(#define\s+)([\d\w]*\s+)([\(\)\*\\\w\s]*)")
        try:
            # Open file in read write mode 
            self.file = open(fileName, "r+t")
#            self.fileCont = self.file.read()
#            print self.fileCont
#            self.file.seek(0)
            self.ExamineFile()
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
    
    def __del__(self):
        print "Distruttore"
        self.file.close()
        
    def getPreemption(self):
        return int(self.freeRTOS_Params['configUSE_PREEMPTION'])
    
    def setPreemption(self, preemptValue):
        print "setPreemption" + str(preemptValue)
        if (preemptValue):
            self.freeRTOS_Params['configUSE_PREEMPTION'] = '1\n'
        else:
            self.freeRTOS_Params['configUSE_PREEMPTION'] = '0\n'
        print self.freeRTOS_Params

    def getUseIdleHook(self):
        return int(self.freeRTOS_Params['configUSE_IDLE_HOOK'])
    
    def setUseIdleHook(self, useIdleHookValue):
        print "setUseIdleHook" + str(useIdleHookValue)
        if (useIdleHookValue):
            self.freeRTOS_Params['configUSE_IDLE_HOOK'] = '1\n'
        else:
            self.freeRTOS_Params['configUSE_IDLE_HOOK'] = '0\n'
        print self.freeRTOS_Params

    def getUseTickHook(self):
        return int(self.freeRTOS_Params['configUSE_TICK_HOOK'])

    def setUseTickHook(self, useTickHookValue):
        print "setUseTickHook" + str(useTickHookValue)
        if (useTickHookValue):
            self.freeRTOS_Params['configUSE_TICK_HOOK'] = '1\n'
        else:
            self.freeRTOS_Params['configUSE_TICK_HOOK'] = '0\n'
        print self.freeRTOS_Params
        
    def ExamineFile(self):
#        self.pattern = re.compile(r"\(\s\([a-zA-Z0-9_ \t\n\r\f\v]*\)[a-zA-Z0-9_ \t\n\r\f\v]*\)")
        self.freeRTOS_Params = {}
        for line in self.file:
            for param in self.freeRTOSParametersName:
                if param in line:
                    print "Find param=" + param + " in " + line
#                    result = self.pattern.search(line)
#                    print result
#                    if result:
#                        print "MATCH: " + result.group()
                    
                    result = self.parameterDefinition.match(line)
                    if result:
                        print "Match 1 " + result.group() + "-d-" + result.group(0) 
                        print "-p-" + result.group(1) + "-v-" + result.group(2) + "-?-" + result.group(3)
                        # Check if parameter is defined in the current line
                        if (param in result.group(2)):
                            print "Param " + param + " defined in line " + line
                            # It's a define: add the value to the list
                            self.freeRTOS_Params .__setitem__(param, result.group(3))
                            
        print "Dictionary " 
        print self.freeRTOS_Params
    
    def SaveFile(self):
        #TODO: Debug ...
        fileBuffer = ''
        self.file.seek(0)
        for line in self.file:            
            for param in self.freeRTOSParametersName:
                if param in line:
                    print "Find param=" + param + " in " + line
                    result = self.parameterDefinition.match(line)
                    if result and (param in result.group(2)):
                        line = result.group(1) + "\t" + result.group(2) + self.freeRTOS_Params[param]
                        print "New line: " + line
            fileBuffer += line
        print "File :"
        print fileBuffer
        self.file.seek(0)
        self.file.write(fileBuffer)
