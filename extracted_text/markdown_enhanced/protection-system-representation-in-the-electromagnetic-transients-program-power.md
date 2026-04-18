# PROTECTION SYSTEM REPRESENTATION IN THE ELECTROMAGNETIC TRANSIENTS PROGRAM

**Arvind K. S. Chaudhary**  
Sargent & Lundy  
Chicago, IL  

**Kwa-Sur Tam and Arun G. Phadke**  
Bradley Department of Electrical Engineering  
Virginia Tech  
Blacksburg, VA  

**Abstract** - This paper concerns the addition of the few critical elements of a protection system to the Electromagnetic Transients Program (EMTP), which is one of the most widely used programs for the simulation of transients in power systems. It contains models for almost every major power system component. A protection system consists of instrument transformers, relays, and circuit breakers.

Models for current transformers (CTs) and capacitor voltage transformers (CVTs) are developed, validated, and incorporated in the EPRI/DCG EMTP Version 2.0. The user can define the values of the CT and CVT parameters. Total FORTRAN capability has been added to the EMTP; new subroutines and an inbuilt structure to allow the linking of user-defined FORTRAN subroutines with the main EMTP are explained. This capability is necessary to simulate computer relay algorithms. The outputs of the algorithms can be passed to the EMTP, which enables the study of the dynamic interaction between the power system and the protection system. The FORTRAN capability can also be used to develop models for relays.

Models of specific relays, such as those for line protection (CEY51A and SLY12C) and transformer differential protection (D202 and BDD15B), are also available. The relay models can be used with different settings.

These new features in the EMTP together constitute the critical elements of a protection system. Thus, it is now possible to simulate the dynamic interactions between a power system and a protection system.

**Keywords** - current transformer (CT) model, capacitor voltage transformer (CVT) model, distance relays, protection system simulation, Electromagnetic Transients Program (EMTP), CT simulation, CVT simulation.

## INTRODUCTION

A protection system consists of instrument transformers, relays, and circuit breakers. Protection systems are critical power system components, and their behavior often determines the response of a power system to a transient event.

Power system response to faults and other sudden disturbances includes transient and steady-state components. For low-speed protection systems, the transient component is generally ignored; only the steady-state component is used for analysis. For high-speed protection systems, the transient and steady-state components must be considered, because the relays operate during the transient regime, which creates a serious risk to protection system security and dependability.

Designers of protection equipment have developed miniature system models to determine relay response under selected system conditions. As with other studies using miniature system models, it is not possible to include substantial portions of the power system in the model. Also, it is not possible to easily vary parameters, such as the remanent flux in the current transformer, the magnetization curve of the current transformer, or the inertia of the machines in the system. Consequently, the dynamics of the interaction between the power system and the protection system cannot be studied. The time required for and the cost of such studies may also be prohibitive.

The Electromagnetic Transients Program (EMTP) is a large computer program for simulating electromagnetic, electromechanical, and control system transients on multiphase electric power systems. This large (more than 100,000 lines) and complex FORTRAN code has been developed over the last 25 years by many individuals. Almost every major power system component is modeled, including nonlinear elements such as circuit breakers and surge arresters. The capabilities of this program for conducting engineering studies are enormous and include insulation coordination, equipment ratings, and the ability to solve operating problems such as unexplained events or equipment failures. The EMTP is also one of the most widely used packages in the electric utility industry [1].

There is a need to study the transient response of the protection system in conjunction with the transient response of the power system, because of the strong interaction between the two systems. For example, a fault on one of the two parallel transmission lines leads to the opening of the faulted line, with the consequent overload and opening of the unfaulted line, which in turn leads to system overvoltages. It is indeed critical for relays to isolate faults, but it is equally important that only the desired relays operate and not the backup relays. With the ever-growing importance of sophisticated computer relay algorithms, a technique must be developed to allow the algorithms to process the power system data and feed back the relay decisions concerning the state of the power system. There is no tool at present that can simulate the dynamic interactions between a power system and a protection system. This paper is a contribution to the effort to develop a few critical protection system components and to integrate them within the EMTP, leading to an enhanced simulation capability.

## RELAY AND PROTECTION SYSTEM TESTING

The simplest method of testing relays consists of supplying the relays with steady-state currents and voltages and plotting the steady-state relay operating characteristics and operating time. No dc offset or reflection transients are applied to the relay. However, in the field a relay initially "sees" the normal power system currents and voltages, and on the occurrence of a fault "sees" the changes in currents and voltages applied to it. Thus, the dynamic operating and not the steady-state characteristics are applicable. The relay in the field is subjected to both the dc offset and the reflection transients. The actual field current and voltage waveforms are essential to testing the relay correctly.

Fig. 1 is similar to Fig. 2 of [2] and lists some of the methods of the relay testing. One method of testing the relay is to take the EMTP data case output, convert it to analog signals, amplify these signals through current and voltage amplifiers, and then feed the relay with them. Another method consists of using the transient network analyzer (TNA).

These methods are useful for testing individual relays in relatively simple configurations. It is often