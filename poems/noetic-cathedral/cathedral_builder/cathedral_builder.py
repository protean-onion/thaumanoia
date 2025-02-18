class CathedralBuilder:
    """
    A class to simulate the existential process of 'cathedralizing' reality.
    Methods model the askesis (disciplined perception) and poiesis (meaning-making) described in the poem.
    """
    
    def __init__(self, struggles: list, perceptions: int = 0):
        self.struggles = struggles  # Life's raw materials (grief, doubt, desire)
        self.perceptions = perceptions  # Current level of phenomenological attention
        self.cathedral = []  # The constructed meaning
        
    def grind_lens(self, epochs: int):
        """Simulate Husserlian epochē - bracketing assumptions to refine perception"""
        for _ in range(epochs):
            self.perceptions += sum(struggle.depth for struggle in self.struggles)
        return self.perceptions
    
    def find_keystones(self):
        """Kierkegaardian function: transform paradoxes into structural elements"""
        return [f"YES_{hash(str(struggle))}" for struggle in self.struggles]
    
    def build_arch(self, material: str):
        """Heideggerian being-in-the-world: enact meaning through doing"""
        if self.perceptions > 100:
            self.cathedral.append(f"ARCH_{material}_UNDERSTOOD")
        else:
            self.cathedral.append(f"CRACKED_{material}_UNSEEN")
    
    def baptize_mundane(self, object):
        """Sacramentalize the ordinary through attention"""
        return f"SACRED_{object.upper()}"
    
    def construct_cathedral(self):
        """Execute the existential algorithm"""
        keystones = self.find_keystones()
        for stone in keystones:
            self.build_arch(stone)
            
        # Nietzschean eternal recurrence: rebuild with same materials
        while len(self.cathedral) < len(self.struggles)*2:
            self.grind_lens(1)
            self.build_arch("PARADOX")
            
        return "CATHEDRAL_BUILT" if self.cathedral else "ABYSS"
    
    def __str__(self):
        """Beckettian output: always unfinished, always becoming"""
        return f"""
        CATHEDRAL OF MEANING v.{self.perceptions}
        -------------------------
        Blueprint: {len(self.struggles)} struggles
        Arches: {sum(1 for x in self.cathedral if 'ARCH' in x)}
        Cracks: {sum(1 for x in self.cathedral if 'CRACKED' in x)}
        Sacred Objects: {self.baptize_mundane('rust')}, {self.baptize_mundane('rain')}
        """

# Initialize with life's struggles
builder = CathedralBuilder(struggles=["loss", "doubt", "joy", "yearning"])

# Execute phenomenological training
builder.grind_lens(epochs=3)  # Equivalent to years of askesis

# Build meaning through iterative existential labor
builder.construct_cathedral()

print(builder)