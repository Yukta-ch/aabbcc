
Aim: Install and understand Docker container, Node.js, Java and Hyperledger 
Fabric, Ethereum and perform necessary software installation on local 
machine/create instance on Cloud to run.

Background Information:
 Background Information:
 Docker: 
 • Docker is a set of platforms as a service (PaaS) product that an OS-level 
    virtualization software platform that helps users in building and managing 
    applications in the Docker environment with all its library dependencies. 
 • Docker is considered a better alternative to a virtual machine. It was first 
   released in 2013 and is developed by Docker, Inc.
 • Docker is a tool that is used to automate the deployment of applications in 
   lightweight containers so that applications can work efficiently in different 
   environments in isolation.

 The main components of Docker are:
 1. Images: 
   An image contains everything your software needs to run - it's the 
   blueprint for creating containers.
 2. Containers: 
   These are the actual instances created from images. 
   They are isolated environments that contain your software and everything 
   it needs, ensuring the software runs consistently across different 
   environments.
 3. Docker Engine: 
   This is the heart of Docker. 
   It's the tool that manages images and containers, allowing you to create, 
   run, and manage them on your computer or in the cloud.
   Docker makes it easy to build, ship, and run applications reliably and efficiently 
   because these containers work the same way no matter where they're running -
   on your laptop, a server, or in the cloud. 


 Installation steps:
 1. Download Docker: Go to the Docker website and download the appropriate 
    Docker installer for your operating system. Or download docker from here, 
    https://www.docker.com/products/docker-desktop/ 
 2. Install Docker: Follow the on-screen instructions to install Docker.
 3. Verify installation: Open a terminal window (command prompt) and run the following 
  Command 1: #docker version
 4. Start the Docker daemon: The Docker daemon is the service that runs Docker containers.
 5. Test Docker: To test Docker, run the following command:
    Command 2: #docker run hello-world
 6. Pull a UBUNTU image from docker hub and run the CentOS container.Make sure the Docker daemon is running.
 7. Pull a UBUNTU image from docker hub and run.
   Command 3: #docker pull ubuntu 
               #docker run -it ubuntu
 8. Now Install and understand Hyperledger Fabric and Ethereum.
    Command 4:
           apt-get update && apt-get install -y \
         software-properties-common \
          curl \
          wget \
          unzip \
          git \
          apt-utils \
          build-essential \
          gcc \
          g++ \
         make

        curl -sL https://deb.nodesource.com/setup_20.x | bash -
        apt-get install -y nodejs
        apt-get install -y openjdk-11-jdk
        add-apt-repository ppa:ethereum/Ethereum
        apt-get update -y
        apt-get install -y solc
        wget https://go.dev/dl/go1.21.3.linux-amd64.tar.gz
        tar -C /usr/local -xzf go1.21.3.linux-amd64.tar.gz
        rm go1.21.3.linux-amd64.tar.gz

       apt-get install -y \
        docker.io \
       libtool \
        libltdl-dev \
        libssl-dev \
        autoconf \
        automake \
        bison \
        libboost-all-dev \
        libgflags-dev \
       libprotobuf-dev \
        libleveldb-dev \
        libsnappy-dev \
        libsodium-dev \
        liblz4-tool
        service --status-all


  Conclusion:
    Thus, the installation of Docker container, Node.js, Java is successfully 
    completed.


