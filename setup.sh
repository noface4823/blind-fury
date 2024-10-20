#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading system..."
sudo apt update -y && sudo apt upgrade -y

# Install dependencies
echo "Installing dependencies..."
sudo apt install git wget curl python3 python3-pip -y

# Install GoLang
echo "Installing GoLang..."
sudo apt install golang -y
mkdir -p $HOME/go/{bin,src,pkg}
echo "export GOPATH=$HOME/go" >> ~/.zshrc
echo "export PATH=$GOPATH/bin:$PATH" >> ~/.zshrc
source ~/.zshrc

# Install URO
echo "Installing URO..."
pip3 install uro --break-system-packages|| { echo "URO installation failed"; exit 1; }

# Install Katana
echo "Installing Katana..."
go install github.com/projectdiscovery/katana/cmd/katana@latest || { echo "Katana installation failed"; exit 1; }

# Install BXSS
echo "Installing BXSS..."
go install github.com/ethicalhackingplayground/bxss@latest || { echo "BXSS repository clone failed"; exit 1; }


# Install GF and GF Patterns
echo "Installing GF and GF Patterns..."
go install github.com/tomnomnom/gf@latest || { echo "GF installation failed"; exit 1; }
mkdir -p ~/.gf
git clone https://github.com/1ndianl33t/Gf-Patterns || { echo "GF Patterns repository clone failed"; exit 1; }
mv Gf-Patterns/*.json ~/.gf

# Install Subfinder
echo "Installing Subfinder..."
a
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# path
sudo cp $HOME/go/bin/* /usr/bin/
# Cleanup
echo "Cleaning up..."
sudo apt autoremove -y

echo "Installation and setup complete!"
