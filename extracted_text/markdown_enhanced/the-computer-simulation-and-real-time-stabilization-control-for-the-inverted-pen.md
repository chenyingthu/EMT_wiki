# The Computer Simulation and Real-time Stabilization Control for the Inverted Pendulum System Based on LQR

**Hu Lingyan**$^{1,2}$, **Liu Guoping**, **Liu Xiaoping**, **Zhang Hua**  
1. School of Mechanical and Electrical Engineering, Nanchang University, Nanchang, China  
2. School of Information and Engineering, Nanchang University, Nanchang, China  
*Email:* hulingyan@ncu.edu.cn, liuguoping@ncu.edu.cn

**Abstract**—The paper established mathematical model of inverted pendulum system, based on the elaborate mechanical analysis. According linear quadratic optimal control theory, the paper put forward an Linear Quadratic Regulator(LQR) for the system. The simulation result shows that the inverted pendulum system with the state feedback matrix can realise the pendulum angle and the carriage position stabilization control. In addition, the real-time control of the pendulum has been accomplished successfully based on the real-time control model built in Simulink. The result of real-time control experiment is simular to the simulation, which also validated the correctness of the theoretical analysis and the rightness of the computer simulation. In addition, comparison analysis between the simulation and real-time control experiment is carried out.

**Keywords**— Inverted pendulum; Simulation; Real-time control; LQR

## I. INTRODUCTION

Inverted pendulum is a nonlinear, coupling, variable and natural unsteadiness system. During the control process, pendulum can effectively reflect many pivotal problems such as equanimity, robust, follow-up and track. Therefore, it is often used as a benchmark for verifying the performance and effectiveness of a new control method because of the simplicities of the structure.

The difficulty of inverted pendulum control is swing-up control. There are many research achievements about it now, but most of the researches are on the premise of that the track of the carriage is long enough and the setting time is very long in many papers, especially controlled by intelligent controllers[1,2,3].

The controller put forward in the paper is Linear Quadratic Regulator(LQR). It is based on the linear theory, so its response is fast and the setting time is short. Although there are many papers about inverted pendulum control with LQR[4,5], they are always limited in theoretic analysis and computer simulation and the real-time control is seldom involved.

At first, the paper established mathematical model of inverted pendulum, based on the detail mechanical analysis on the inverted pendulum system. Secondly, the LQ optimal regulator is designed according the theoretical model. Then computer simulation is carried out. Finally we applied the parameters which result in good performance in simulation experiments to physical control experiment. The real-time experiment result shows the controller can realized the angle and position control in parallel in a short time. Furthermore, comparison is carried out between the simulation and real-time control.

## II. MATHEMATICAL MODEL FOR THE INVERTED PENDULUM

The inverted pendulum mainly consists of a carriage, a pendulum, a rail for defining the position of the carriage and a driving unit. The pendulum is hinged in the center of the top of the carriage and can rotate around the pivot in the same vertical plane with the rail. The carriage can move right or left on the rail freely. The physical model for the inverted pendulum is shown is Fig. 1-a. It is given that 1)no friction exists in the system between the carriage and the rail or between the carriage and the pendulum; 2)Pendulum and carriage are rigid bodies; carriage is as a particle; 3) no relative sliding between the belt and the pulley, etc.

The mechanical analysis of the inverted pendulum is shown as Fig. 1-b and Fig. 1-c.

Here, $g=9.8\text{m/s}^2$ is the gravity acceleration. The variable $F$ means the driving force in the unit [N] applied horizontally to the carriage. The variables $\theta$, $\dot{\theta}$ represent, respectively, the angle of the pendulum from upright position, its angular velocity, and the clockwise direction is positive. $\theta=\pi+\phi$. The variables $x$, $\dot{x}$ denote the position of the carriage from the rail origin, its velocity, and right direction is positive. The other symbols are listed in Tab. 1.

The friction appearing in the motion of the carriage is proportional to its velocity, and the friction coefficient is $b$.

Analyzing the horizon force of the carriage, equation (1) is obtained.

$$M\ddot{x} = F - b\dot{x} - N \tag{1}$$

Where $X = [x, \dot{x}, \phi, \dot{\phi}]^T$, $u = F$,

$$A = \begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & -\frac{(I+ml^2)b}{I(M+m)+Mml^2} & \frac{m^2gl^2}{I(M+m)+Mml^2} & 0
\end{bmatrix}$$

According the force applied horizontally to the