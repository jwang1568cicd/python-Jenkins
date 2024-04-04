Vagrant.configure("2") do |config|
config.vm.define "nexus" do |nexus| 
        nexus.vm.box = "centos/7" 
        nexus.vm.hostname = "nexus" 
        nexus.vm.network "private_network", ip: "192.168.5.2" 
        config.vm.provision "shell", inline: "ifup enp0s8", run: "always" 
  end 

  config.vm.define "sonar" do |sonar| 
        sonar.vm.box = "geerlingguy/ubuntu2004" 
        sonar.vm.hostname = "sonar" 
        sonar.vm.network "private_network", ip: "192.168.5.3" 
  end 

  config.vm.define "jenkins" do |jenkins| 
        jenkins.vm.box = "geerlingguy/ubuntu2004" 
        jenkins.vm.hostname = "jenkins" 
        jenkins.vm.network "private_network", ip: "192.168.5.5" 
  end 
  config.vm.define "redisclient" do |redisclient|
        redisclient.vm.box = "geerlingguy/ubuntu2004"
        redisclient.vm.hostname = "redisClient"
        redisclient.vm.network "private_network", ip: "192.168.7.55"
  end
  config.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      # vb.gui = true
      # vb.grub_menu_key = "c"

      # Customize the amount of memory on the VM:
      vb.memory = "2048"
      vb.cpus = "2"
  end
end
