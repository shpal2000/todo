#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------
FROM ubuntu:focal

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root 'vscode' user with sudo access. However, for Linux,
# this user's GID/UID must match your local user UID/GID to avoid permission issues
# with bind mounts. Update USER_UID / USER_GID if yours is not 1000. See
# https://aka.ms/vscode-remote/containers/non-root-user for details.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Configure apt and install packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -yq install apt-utils \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -yq install git iproute2 procps lsb-release \
    #
    && apt-get -yq install iputils-ping netcat tcpdump \
    #
    && apt-get -yq install pkg-config \
    && apt-get -yq install python3-pip meson curl \
    && apt-get -yq install vim \
    && apt-get -yq install sshpass net-tools \
    #
    && apt-get -yq install tmux \
    && echo "test" > /root/.tmux-buffer \
    && echo "set -g status off" > /root/.tmux.conf \
    && echo "set -g mouse on" >> /root/.tmux.conf \
    && echo "set -g prefix C-b" >> /root/.tmux.conf \
    && echo "bind C-b send-prefix" >> /root/.tmux.conf \
    && echo "unbind-key C-f" >> /root/.tmux.conf \
    && echo "unbind-key C-a" >> /root/.tmux.conf \
    && echo "setw -g mode-keys vi" >> /root/.tmux.conf \
    && echo "set -g base-index 1" >> /root/.tmux.conf \
    && echo "setw -g pane-base-index 1" >> /root/.tmux.conf \
    && echo "set -g pane-active-border-style bg=default,fg=colour250" >> /root/.tmux.conf \
    && echo "set -g pane-border-style fg=colour250" >> /root/.tmux.conf \
    && echo "set -g status" >> /root/.tmux.conf \
    && echo "set -g status-right ''" >> /root/.tmux.conf \
    && echo "set -g status-bg colour255" >> /root/.tmux.conf \
    && echo "set -g status-fg colour246" >> /root/.tmux.conf \
    && echo "set-window-option -g window-status-current-style fg=colour9" >> /root/.tmux.conf \
    && echo "set-window-option -g window-status-style fg=colour100" >> /root/.tmux.conf \
    && echo "bind P paste-buffer" >> /root/.tmux.conf \
    && echo "bind-key -T copy-mode-vi v send-keys -X begin-selection" >> /root/.tmux.conf \
    && echo "bind-key -T copy-mode-vi y send-keys -X copy-selection" >> /root/.tmux.conf \
    && echo "bind-key -T copy-mode-vi r send-keys -X rectangle-toggle" >> /root/.tmux.conf \
    && echo "bind-key p save-buffer ~/.tmux-buffer" >> /root/.tmux.conf \
    #
    # Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support for the non-root user
    && apt-get install -yq sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    #
    # Clean up
    && apt-get autoremove -yq \
    && apt-get clean -yq \
    && rm -rf /var/lib/apt/lists/* 
RUN pip3 install fastapi uvicorn orjson python-dotenv requests pytest
# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=
