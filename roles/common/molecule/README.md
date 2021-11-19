### Common molecule testing

### Dependencies 


Docker - https://docs.docker.com/get-docker/


### Python dependencies
Testing modules:
  - molecule[docker,lint]
  - yamllint 
  - ansible-lint
  - pytest-testinfra


```
apt install ansible-lint yamllint
python3 -m pip install --user "molecule[docker,lint], pytest, testinfra"
```

### Running
`molecule create`   
`molecule converge`    
`molecule verify`    
`molecule destroy`    

*all of the above in one shot*   
`molecule test` 

### Docs
https://molecule.readthedocs.io/en/latest/