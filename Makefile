PKG_NAME := jdk-groovy
URL := http://repo1.maven.org/maven2/org/codehaus/groovy/groovy/2.4.5/groovy-2.4.5.jar
ARCHIVES := http://repo1.maven.org/maven2/org/codehaus/groovy/groovy/2.4.5/groovy-2.4.5.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.5/groovy-all-2.4.5.jar %{buildroot} \
	http://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.5/groovy-all-2.4.5.pom %{buildroot}

include ../common/Makefile.common
