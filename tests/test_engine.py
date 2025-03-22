import unittest
from src.engine import PolymorphicEngine

class TestPolymorphicEngine(unittest.TestCase):
	def setUp(self):
		self.engine = PolymorphicEngine()
		self.test_shellcode = b"\x90\x90\x90\x90"  # NOP sled
		
	def test_mutation(self):
		mutated = self.engine.mutate(self.test_shellcode)
		self.assertNotEqual(mutated, self.test_shellcode)
		self.assertGreater(len(mutated), len(self.test_shellcode))
		
	def test_encryption(self):
		encrypted = self.engine.encrypt(self.test_shellcode)
		decrypted = bytes([b ^ self.engine.key[i % len(self.engine.key)] 
						  for i, b in enumerate(encrypted)])
		self.assertEqual(decrypted, self.test_shellcode)
		
	def test_decryptor_stub(self):
		stub = self.engine.generate_decryptor_stub()
		self.assertTrue(b"\x48\x31\xc9" in stub)  # Check for XOR RCX,RCX
		
if __name__ == "__main__":
	unittest.main()