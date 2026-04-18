# Creating an Electromagnetic Transients Program in MATLAB: MatEMTP

**Jean Mahseredjian** (IEEE member)  
*Institut de Recherche d'Hydro-Quebec (IREQ)*  
1800 Montee Ste-Julie  
Varennes, Quebec, Canada J3X 1S1  

**Fernando Alvarado** (IEEE fellow member)  
*University of Wisconsin-Madison*  
Electrical & Computer Engineering  
1415 Johnson Drive, Madison, WI 53706, USA  

**ABSTRACT:** The traditional method for developing electric network analysis computer programs is based on coding using a conventional computer language: FORTRAN, C or Pascal. The programming language of the EMTP (Electromagnetic Transients Program) is FORTRAN-77. Such a program has a closed architecture and uses a large number of code lines to satisfy requirements ranging from low level data manipulation to the actual solution mathematics which eventually become diluted and almost impossible to visualize. This paper proposes a new design idea suitable for EMTP re-development in a high level programming context. It presents the creation of the transient analysis numerical simulator MatEMTP in the computational engine frame of MATLAB. This new approach to software engineering can afford a dramatic coding simplification for sophisticated algorithmic structures.

**Keywords:** EMTP, MATLAB, time-domain network analysis, software engineering

In a conventional electric network simulator design, everything is based on line-by-line coding. Every component is implemented this way, as is the network analysis algorithm and any minor details of the overall computation and data manipulation process. The actual network model equations and network matrix operations are diluted in a large number of cryptic code lines created by specialized and experienced developers. Moreover, old-fashioned and historically supported programming techniques inhibit modularity and are geared towards memory conservation. Models for any one component appear in more than one place in the code. This is the case of the EMTP [1] (Electromagnetic Transients Program) code. The low level design methodology of such a code explains its low renewal and enhancement rate. It is also prohibitive to experiment with modern algorithmic ideas for eliminating solution limitations or for improving the computational speed on changing computer architectures.

Most network solution and modelling methods are simple to visualize and support mathematically, but their translation into an actual large scale working code is complex. Commonly used programming languages are ill-suited to human abilities for dealing with complexity. Software built using such languages is often inadequate. Some other new languages such as ADA, C++ and FORTRAN-90, provide powerful features for the formulation of appropriate abstractions [2] for the desired application. But programming is always easier if a specialized language is already available for the creation of similar applications. Specialized applications should use dedicated computational engines where the developer can build and compose with high level constructs. In addition to defining a new library of functions and overloading existing operators, such an engine must provide a minimal number of portable graphical data visualization and manipulation functions. It is obvious that programming a computational engine from scratch is a major effort.

This paper proposes to use a widely used general purpose program available on most popular computer platforms as a computational engine: MATLAB [3]. MATLAB has a large number of built-in functions and constructs covering a wide range of EMTP development needs and is expandable by means of optional toolboxes. The recent implementation of sparse matrix manipulation capabilities eliminates a major feasibility barrier.

This paper presents the creation of MatEMTP: a transient analysis program in MATLAB M-files. It is based on a new formulation of the main system of network equations, designed to eliminate several topological data restrictions and capable of handling arbitrary switch interconnections. The existing EMTP is used for validation and as a reference for solution timings.

## 2. SOLUTION METHOD

The basic time-domain solution method implemented in MatEMTP is similar to the existing EMTP approach [4]. A large set of algebraic-differential equations is first transformed into a discrete algebraic equivalent and then solved over the requested interval $[0, t_{\max}]$. The solution is available at discrete time-points $(0, t_1, t_2, \dots, t_{\max})$. The design utilizes a fixed integration time-step $\Delta t$ as is the case for EMTP.

The high level matrix manipulation capabilities of MATLAB stimulate algorithmic ideas based on matrix computations. MatEMTP uses matrices and vectors for coding and solving network equations, closely replicating the underlying

### 2.c Component models

Network models consist of an interconnection of component models. Component models interact with the core code by inserting their frequency domain and time-domain equations into (1). Node incidence ma