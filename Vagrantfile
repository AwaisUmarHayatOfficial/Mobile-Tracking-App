Vagrant.configure("2") do |config|
  BOX = "bento/ubuntu-24.04"

  # -----------------
  # Master Node
  # -----------------
  config.vm.define "MasterNode" do |master|
    master.vm.box = BOX
    master.vm.hostname = "MasterNode"
    master.vm.network "private_network", ip: "192.168.56.10"

    # Port Forwarding
    master.vm.network "forwarded_port", guest: 80, host: 8080
    master.vm.network "forwarded_port", guest: 8081, host: 8081
    master.vm.network "forwarded_port", guest: 8082, host: 8082
    master.vm.network "forwarded_port", guest: 8083, host: 8083
    master.vm.network "forwarded_port", guest: 8084, host: 8084

    master.vm.provider "virtualbox" do |vb|
      vb.name = "Master Node"
      vb.memory = 4096
      vb.cpus = 2
    end
  end


  # -----------------
  # Worker Node
  # -----------------
  config.vm.define "WorkerNode" do |worker|
    worker.vm.box = BOX
    worker.vm.hostname = "WorkerNode"
    worker.vm.network "private_network", ip: "192.168.56.11"

    # Port Forwarding (different host ports to avoid conflict)
    worker.vm.network "forwarded_port", guest: 8080, host: 8090
    worker.vm.network "forwarded_port", guest: 8081, host: 8091
    worker.vm.network "forwarded_port", guest: 8082, host: 8092
    worker.vm.network "forwarded_port", guest: 8083, host: 8093
    worker.vm.network "forwarded_port", guest: 8084, host: 8094

    worker.vm.provider "virtualbox" do |vb|
      vb.name = "Worker Node"
      vb.memory = 4096
      vb.cpus = 2
    end
  end
end
