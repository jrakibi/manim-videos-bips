from manim import *

class BitcoinTransactionScene(Scene):
    def construct(self):
        # Create a simple character (stick figure)
        character = self.create_character()
        
        # Create a thought bubble from PNG
        thought_bubble = self.create_png_thought_bubble()
        
        # Create multi-line text with WHITE color
        bubble_text = Text("How Bitcoin\nTransaction Works", 
                          font_size=16, 
                          color=WHITE,  # Changed to WHITE
                          line_spacing=1)
        
        # Position the character and thought bubble
        character.to_corner(LEFT + DOWN)
        thought_bubble.next_to(character, UP + RIGHT, buff=0.5)
        
        # Position text inside the thought bubble
        bubble_text.move_to(thought_bubble.get_center())
        
        # Show the character thinking - with proper sequence
        self.play(FadeIn(character))
        self.play(FadeIn(thought_bubble))
        
        # Wait a moment before showing text to ensure bubble is fully visible
        self.wait(0.5)
        
        # Now show the text
        self.play(Write(bubble_text))
        
        # Hold the scene for a moment
        self.wait(2)
    
    def create_character(self):
        # Create a simple stick figure
        head = Circle(radius=0.3, color=WHITE, fill_opacity=0)
        body = Line(DOWN * 0.3, DOWN * 1.5)
        arms = VGroup(
            Line(DOWN * 0.7, DOWN * 0.7 + LEFT * 0.5),
            Line(DOWN * 0.7, DOWN * 0.7 + RIGHT * 0.5)
        )
        legs = VGroup(
            Line(DOWN * 1.5, DOWN * 2.2 + LEFT * 0.5),
            Line(DOWN * 1.5, DOWN * 2.2 + RIGHT * 0.5)
        )
        
        character = VGroup(head, body, arms, legs)
        return character
    
    def create_png_thought_bubble(self):
        # Import PNG file - replace with your actual PNG file path
        thought_bubble = ImageMobject("assets/thought_bubble.png")
        
        # Scale as needed
        thought_bubble.scale(1)  # Adjust scale as needed
        
        return thought_bubble
    
    def explain_bitcoin_transaction(self, thought_bubble):
        # Create all the elements for the Bitcoin transaction explanation
        main_bubble = thought_bubble[1]
        
        # Setup the transaction elements
        title = Text("Bitcoin Transaction", font_size=24)
        title.to_edge(UP).shift(RIGHT * 2)
        
        # Wallet addresses
        wallet_a = RoundedRectangle(height=0.8, width=1.5, corner_radius=0.1)
        wallet_a_text = Text("Alice's Wallet", font_size=18)
        wallet_a_text.move_to(wallet_a)
        wallet_a_group = VGroup(wallet_a, wallet_a_text)
        
        wallet_b = RoundedRectangle(height=0.8, width=1.5, corner_radius=0.1)
        wallet_b_text = Text("Bob's Wallet", font_size=18)
        wallet_b_text.move_to(wallet_b)
        wallet_b_group = VGroup(wallet_b, wallet_b_text)
        
        # Position wallets
        wallet_a_group.move_to(main_bubble.get_center() + LEFT * 1.5 + UP * 0.5)
        wallet_b_group.move_to(main_bubble.get_center() + RIGHT * 1.5 + UP * 0.5)
        
        # Transaction arrow
        arrow = Arrow(wallet_a_group.get_right(), wallet_b_group.get_left(), buff=0.2)
        btc_text = Text("0.05 BTC", font_size=16)
        btc_text.next_to(arrow, UP, buff=0.1)
        
        # Digital signature and verification
        signature_box = Rectangle(height=0.6, width=1.2)
        signature_text = Text("Digital Signature", font_size=14)
        signature_text.move_to(signature_box)
        signature_group = VGroup(signature_box, signature_text)
        signature_group.next_to(arrow, DOWN, buff=0.2)
        
        # Blockchain
        blockchain = self.create_blockchain()
        blockchain.move_to(main_bubble.get_center() + DOWN * 1.2)
        blockchain.scale(0.8)
        
        # Animate the transaction explanation
        self.play(
            FadeIn(title, target_position=main_bubble.get_center()),
            run_time=1
        )
        
        self.play(
            Create(wallet_a_group),
            Create(wallet_b_group),
            run_time=1.5
        )
        
        self.play(
            GrowArrow(arrow),
            FadeIn(btc_text),
            run_time=1
        )
        
        self.play(
            Create(signature_group),
            run_time=1
        )
        
        self.play(
            FadeIn(blockchain),
            run_time=1.5
        )
        
        # Show transaction being added to blockchain
        transaction_block = Rectangle(height=0.4, width=0.5, color=YELLOW)
        transaction_block.move_to(blockchain.get_right() + RIGHT * 0.3)
        
        self.play(
            Create(transaction_block),
            run_time=0.8
        )
        
        self.play(
            transaction_block.animate.move_to(blockchain.get_right() + RIGHT * 0.01),
            run_time=1
        )
        
        self.play(
            Flash(transaction_block, color=GREEN, line_length=0.2, flash_radius=0.3),
            run_time=0.5
        )
        
    def create_blockchain(self):
        # Create a simple blockchain representation
        blocks = VGroup(*[
            Rectangle(height=0.4, width=0.5, color=BLUE)
            for _ in range(5)
        ])
        blocks.arrange(RIGHT, buff=0.05)
        
        # Add connecting lines
        connections = VGroup(*[
            Line(blocks[i].get_right(), blocks[i+1].get_left(), buff=0.01)
            for i in range(len(blocks)-1)
        ])
        
        blockchain = VGroup(blocks, connections)
        blockchain_label = Text("Blockchain", font_size=16)
        blockchain_label.next_to(blockchain, UP, buff=0.2)
        
        return VGroup(blockchain, blockchain_label)