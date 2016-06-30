# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

  config.vm.provision "bootstrap",
    type: "shell",
    privileged: true,
    inline: <<-SHELL
      # development tools
      apt-get install -qy git
      apt-get install -qy jq

      # for converting README.md to README.rst
      apt-get install -qy pandoc

      # test tools
      apt-get install -qy python-pytest

      # packaging tools
      apt-get install -qy python-setuptools
      apt-get install -qy python-pip

      # build/run dependencies
      apt-get install -qy libprotobuf-dev
      apt-get install -qy protobuf-compiler
      apt-get install -qy libprotoc-dev
      apt-get install -qy python-protobuf
    SHELL
end
