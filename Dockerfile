FROM amazon/aws-cli:latest

# COPY ./build/*.crt /etc/pki/ca-trust/source/anchors/cert.ca

# RUN update-ca-trust enable 
# RUN update-ca-trust extract

RUN yum update -y \
    && yum install -y yum-utils shadow-utils \
    && yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo \
    && yum install -y terraform

RUN mkdir ~/.aws && echo -e "[default]\nregion = eu-west-2\noutput = json" > /root/.aws/config
ADD aws-credentials /root/.aws/credentials

WORKDIR /root
ENTRYPOINT /bin/bash

##NotTHIS####COPY ./build/*.crt /usr/local/share/ca-certificates/cert.ca
#COPY ./build/*.crt /etc/pki/ca-trust/source/anchors/cert.ca

#RUN update-ca-trust enable 
#RUN update-ca-trust extract
#####NOTTHIS ### RUN update-ca-certificates

