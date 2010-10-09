package sinsoku.sample;

public class Pystr {
	String str = "";

	public Pystr() {
	}

	public Pystr(String s) {
		this.str = s;
	}

	public Pystr(int i) {
		this.str = String.valueOf(i);
	}

	public Pystr(long l) {
		this.str = String.valueOf(l);
	}

	public Pystr(double d) {
		this.str = String.valueOf(d);
	}

	public Pystr(char c) {
		this.str = String.valueOf(c);
	}

	public Pystr(char[] data) {
		this.str = String.valueOf(data);
	}

	@Override
	public String toString() {
		return str;
	}
}
