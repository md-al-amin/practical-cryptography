from Cryptodome.PublicKey import  RSA

# Generate RSA Public & Private Key & save those into a file
key = RSA.generate(1024)
private_key = key.export_key()
output_file = open("private.pem","wb")
output_file.write(private_key)
public_key = key.publickey().export_key()
output_file = open("public.pem","wb")
output_file.write(public_key)