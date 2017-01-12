Name     : jdk-groovy
Version  : 1
Release  : 1
URL      : http://repo1.maven.org/maven2/org/codehaus/groovy/groovy/2.4.5/groovy-2.4.5.jar
Source0  : http://repo1.maven.org/maven2/org/codehaus/groovy/groovy/2.4.5/groovy-2.4.5.jar
Source1  : http://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.5/groovy-all-2.4.5.jar
Source2  : http://repo1.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.5/groovy-all-2.4.5.pom
Source3  : http://repo1.maven.org/maven2/org/codehaus/groovy/groovy/2.4.5/groovy-2.4.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms/groovy
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java/groovy

mv %{SOURCE0} %{buildroot}/usr/share/java/groovy/groovy.jar
mv %{SOURCE1} %{buildroot}/usr/share/java/groovy/groovy-all.jar
mv %{SOURCE2} %{buildroot}/usr/share/maven-poms/groovy/groovy-all.pom
mv %{SOURCE3} %{buildroot}/usr/share/maven-poms/groovy/groovy.pom

cat %{buildroot}/usr/share/maven-poms/groovy/groovy.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/groovy.xml \
%{buildroot}/usr/share/maven-poms/groovy/groovy.pom \
%{buildroot}/usr/share/java/groovy/groovy.jar \

python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/groovy-all.xml \
%{buildroot}/usr/share/maven-poms/groovy/groovy.pom \
%{buildroot}/usr/share/java/groovy/groovy.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/groovy/groovy-all.jar
/usr/share/java/groovy/groovy.jar
/usr/share/maven-metadata/groovy.xml
/usr/share/maven-metadata/groovy-all.xml
/usr/share/maven-poms/groovy/groovy-all.pom
/usr/share/maven-poms/groovy/groovy.pom
