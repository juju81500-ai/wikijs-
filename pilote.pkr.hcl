packer {
  required_version = ">= 1.16.0"
}

variable "message" {
  type    = string
  default = "pilote-packer"
}

source "null" "pilote" {
  communicator = "none"
}

build {
  name    = "pilote"
  sources = ["source.null.pilote"]

  provisioner "shell-local" {
    inline = ["echo ${var.message}"]
  }
}
