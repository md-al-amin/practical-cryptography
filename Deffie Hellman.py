#Program Diffie Hellman Key excahange
#MD. AL AMIN Email: info3.alamin@gmail.com
#Variable for shared prime & generator
#Programming language =  python version 3.6.3
shared_prime = 23    #p
shared_generator =  5  # g

# Private key for alice  & bob
alice_private_key = 4 # This key is private only alice know this & not shared to anyone
bob_private_key =  3 #  This key is private only bob know this key & not shared to anyone


# after calculating alice shared this key with bob known as session key
alice_session_key   =  (shared_generator ** alice_private_key) % shared_prime
# After calculating bob shared this key with alice known as session key
bob_session_key = (shared_generator ** bob_private_key) % shared_prime

''' Now Alice and Bob calculate the symmetric keys also known as  Shared secrect key used as an
encryption key over open communications channel because this key is not shared over public channel '''
alice_secret_key = (bob_session_key ** alice_private_key) % shared_prime
bob_secret_key = (alice_session_key ** bob_private_key) % shared_prime

# print Publicly shared prime(p)  & Generator (g)
print("Shared Prime = %i  shared Generator %i " %(shared_prime,shared_generator))
print("Alice private key =%i  Bob's private key %i " %(alice_private_key,bob_private_key))
print("Alice Session key = %i  Bob's Session key %i " %(alice_session_key, bob_session_key))
print("Alice shared secret  key =  %i  Bob's Shared secret key = %i \n Shared secret value Can be used as encryption key "
      "over open communication channel because this key is not shared over public channel" %(alice_secret_key, bob_secret_key))


