package dao;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.AnnotationConfiguration;

public class DBOperation {

	static AnnotationConfiguration annotationConfiguration;
	static SessionFactory sessionFactory;
	Session session;
	Transaction transaction;
	Query query;
	List list;

	static {
		annotationConfiguration = new AnnotationConfiguration();
		annotationConfiguration.configure("hibernate.cfg.xml");
		sessionFactory = annotationConfiguration.buildSessionFactory();
	}
	
	public List getListByParams(String hqlQuery, String[] paramNames, String[] paramValues) {
		query = session.createQuery(hqlQuery);
		if(paramNames.length == paramValues.length)
		{
			for(int i=0;i<paramNames.length;i++)
				query.setParameter(paramNames[i], paramValues[i]);
		}
		else
			return null;
		return query.list();
	}

	public void openSession() {
		session = sessionFactory.openSession();
	}

	public void closeSession() {
		session.close();
	}

	public void openSessionWithTransaction() {
		session = sessionFactory.openSession();
		transaction = session.beginTransaction();
	}

	public void closeSessionWithTransaction() {
		transaction.commit();
		session.close();
	}

	public List getList(String hqlQuery) {
		// first call openSession
		query = session.createQuery(hqlQuery);
		return query.list();
	}

	public void insert(Object commonVo) {
		session.save(commonVo);
	}

	public void update(Object commonVo) {
		session.update(commonVo);
	}

	public void updateQuery(String hqlQuery) {
		query = session.createQuery(hqlQuery);
		query.executeUpdate();
	}

	public void delete(String hqlQuery) {
		query = session.createQuery(hqlQuery);
		query.executeUpdate();
	}

	public void delete(Object commonVo) {
		session.delete(commonVo);
	}

	public List getListByParam(String hqlQuery, String masterEmail, String masterPassword, String param1,
			String param2) {
		query = session.createQuery(hqlQuery);
		query.setParameter(param1, masterEmail);
		query.setParameter(param2, masterPassword);
		return query.list();
	}

}
