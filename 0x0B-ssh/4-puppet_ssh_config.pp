# Using Puppet to make changes in configuration file
line { 'Turn off passwd auth':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}

line { 'Declare identity file':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
line => 'IdentifyFile ~/.ssh/holberton',
}

