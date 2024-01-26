
 Aim: Set up MetaMask, set up Ganache, create two accounts with 100 ETH each, and transfer ETH between the accounts.
 
 Background Information:
    These tools are commonly used in the world of Ethereum development and blockchain testing.
    MetaMask:
         MetaMask is like a digital wallet that you can use on the internet. 
         It helps you manage something called cryptocurrency, specifically Ethereum.
         A popular cryptocurrency wallet extension that allows users to interact with the Ethereum blockchain. 
         It stores private keys, connects to different networks (mainnet, testnets), and facilitates transactions.
         It's available as a browser extension and a mobile app. 
      Here's the background:
        • Purpose:
            MetaMask allows users to interact with decentralized applications (dApps) 
            on the Ethereum blockchain and manage their Ethereum-based assets.
        • Features: 
            It provides a secure wallet to store Ether (ETH) and ERC-20 tokens, 
            enables interaction with dApps, and facilitates transactions on the 
            Ethereum network.
        • Setup: 
            Users create an account by installing the MetaMask extension, set up a 
            password, and are given a unique seed phrase that serves as a backup to access their account.

        Ganache:
            Ganache is a tool that helps you practice with fake money on a pretend internet money system called Ethereum. 
            It's like a play area for learning.
            A blockchain simulator used for development and testing. 
            Ganache is a personal blockchain for Ethereum development purposes, provided by the Truffle Suite. 
            It's used for testing smart contracts and dApps. 
         Here's the background:
          • Purpose: 
            Ganache offers a local blockchain environment that developers can use to 
            test their Ethereum-based applications without deploying to the main Ethereum network (which involves real Ether).
          • Features: 
            It generates a set of accounts with ETH, allows for rapid testing and 
            development of smart contracts, and simulates various scenarios on a private blockchain.
          • Setup: 
            Users download and install Ganache, which creates a local blockchain with 
            a set of accounts, each preloaded with test Ether (not real ETH).

    Installation steps:
         Setting up MetaMask:
            1. Install MetaMask:
                 Go to metamask.io and download the MetaMask extension for your web browser (like Chrome, Firefox).
   
           2. Create an Account:
                 • After installation, open MetaMask. 
                 • Follow the instructions to create an account and set a password.
                 • MetaMask will give you a unique 12-word phrase called a seed phrase.
                 • This is super important—keep it safe and don't share it with anyone. It's like the key to your wallet.

          Setting up Ganache:
                 Ganache is a tool for creating a private blockchain to experiment with without using real money.
             1. Download Ganache: 
                 Visit the Truffle Suite website and download Ganache. 
                 It's available for Windows, macOS, and Linux.
             2. Install and Run: 
                Once downloaded, install Ganache and open the application. 
                It'll set up a private blockchain for you to use.

        Creating Accounts with 100 ETH Each:
             Now, let's connect MetaMask to the Ganache private blockchain and create accounts with fake ETH.
             1. Connect MetaMask to Ganache:
                To create a network: 
                   Setting ->Network ->Add a Network ->Add a network manually.
                   Enter the details provided by Ganache, like RPC Server, Chain ID, etc.
             2.Import Accounts: 
                In Ganache, you'll see a list of accounts it generates, each with fake ETH. 
                Import two of these accounts into MetaMask using their private keys.
                Each account starts with 100 fake ETH.
                   1.Open MetaMask in your browser and click on "Import Account."
                   2. Copy the private key of the first account from Ganache and import it into MetaMask by pasting the key.


            Transferring ETH Between Accounts:
                 Let's practice transferring fake ETH between these accounts:
                 1. Access MetaMask: 
                     Make sure you're in the Ganache network on MetaMask.
                 2. Select Sender Account: 
                      Choose the account from which you want to send ETH.
                      In MetaMask, select Account 1.
                 3. Send ETH: 
                    Click on "Send" within MetaMask, enter the recipient's address (the other 
                    account), input the amount you want to send (e.g., 2 ETH), and confirm the transaction.
                 4. Confirm Transaction: 
                     Approve the transaction within MetaMask.
                 5. Check Balances: 
                    After the transaction, check the balances in both accounts in MetaMask and Ganache. 
                    You'll see the ETH balance change accordingly.






