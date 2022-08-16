# Set up the client SSH configuration file so that you can connect
# to a server without typing a password.
# include stdlib

file_line { 'Use private key':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Refuse password':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}
