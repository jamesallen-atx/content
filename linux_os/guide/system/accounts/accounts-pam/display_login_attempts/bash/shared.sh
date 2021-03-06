# platform = Red Hat Virtualization 4,multi_platform_fedora,multi_platform_ol,multi_platform_rhel,multi_platform_wrlinux

if grep -q "^session.*pam_lastlog.so" /etc/pam.d/postlogin; then
	sed -i --follow-symlinks "/pam_lastlog.so/d" /etc/pam.d/postlogin
fi

echo "session     [default=1]   pam_lastlog.so nowtmp showfailed" >> /etc/pam.d/postlogin
echo "session     optional      pam_lastlog.so silent noupdate showfailed" >> /etc/pam.d/postlogin
