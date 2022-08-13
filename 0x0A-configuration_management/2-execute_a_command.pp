# kill a process named killmenow
exec { 'killmenow_process':
    path    => '/usr/bin',
    command => 'pkill -f killmenow',
}
