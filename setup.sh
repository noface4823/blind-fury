#!/bin/bash

# Update the system
echo "Updating system..........."
sudo apt update -y
sudo apt upgrade -y
echo "installing tqdm............"
pip3 install tqdm --break-system-packages


# Install Go (if not installed)
if ! [ -x "$(command -v go)" ]; then
    echo "Go not found, installing Go..."
    sudo apt install -y golang-go
else
    echo "Go is already installed!"
fi

# Install Subfinder
echo "Installing Subfinder..........."
sudo apt install subfinder -y

# Install httpx
echo "Installing httpx..........."
sudo apt install httpx-toolkit -y
# Install Katana
echo "Installing Katana..."
go install -v github.com/projectdiscovery/katana/cmd/katana@latest

# Install gf (Gf Pattern Matching)
echo "Installing gf..........."
go install -v github.com/tomnomnom/gf@latest
echo "Fetching gf patterns..."
git clone https://github.com/1ndianl33t/Gf-Patterns
mkdir -p ~/.gf
cp -r Gf-Patterns/*.json ~/.gf/

# Install BXSS
echo "Installing BXSS..."
go install github.com/Elsfa7-110/bxss@latest

# Add Go bin to PATH if not already added
if ! echo $PATH | grep -q "$HOME/go/bin"; then
    echo "Adding Go bin to PATH..."
    echo "export PATH=$PATH:$HOME/go/bin" >> ~/.bashrc
    source ~/.bashrc
fi

# Check if all tools are installed
echo "Verifying installations..."
for tool in subfinder httpx katana gf bxss; do
    if ! [ -x "$(command -v $tool)" ]; then
        echo "$tool installation failed. Please check manually."
    else
        echo "$tool installed successfully!"
    fi
done

echo "Setup complete!"

