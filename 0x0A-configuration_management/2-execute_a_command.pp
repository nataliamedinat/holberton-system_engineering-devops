# Manifest that kills a process
exec { 'killmenow':
path    => '/usr/bin',
command => 'pkill -f killmenow',
}
