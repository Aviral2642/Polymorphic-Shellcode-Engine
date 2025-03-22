import ctypes
import sys

class EvasionTechniques:
	@staticmethod
	def is_sandbox():
		"""Check for common sandbox artifacts"""
		# Check for VM hypervisor presence
		try:
			cpuid = ctypes.windll.kernel32.IsProcessorFeaturePresent
			if cpuid(0x40000000):  # Hypervisor present
				return True
		except:
			pass
		
		# Check for low RAM (common in sandboxes)
		if sys.platform == 'win32':
			mem = ctypes.c_ulonglong()
			ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(mem))
			return mem.value < 2 * 1024**3  # Less than 2GB RAM?
		return False

	@staticmethod
	def api_hashing(library, function_name):
		"""Resolve APIs via hash to avoid string detection"""
		lib = ctypes.windll.LoadLibrary(library)
		for export in lib._functions:
			if hash(export) == precomputed_hash:
				return getattr(lib, export)
		return None