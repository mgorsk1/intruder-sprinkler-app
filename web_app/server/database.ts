import sqlite3, {Database} from 'sqlite3';
import {emptyUserStats, Message, Statistics} from './types';

export function openDatabase(): Database {
  const db = new sqlite3.Database(':memory:');
  db.run('CREATE TABLE IF NOT EXISTS collections(user text, class text, time text)', (err) => {
    if (err) {
      console.error('Failed to open database!');
      process.exit(1);
    }
  });
  return db;
}

export function insertMessage(db: Database, msg: Message, time: string) {
  db.run('INSERT INTO collections(user, class, time) VALUES (?, ?, ?)', [msg.user, msg.class, time],
    (err) => {
      if (err) {
        console.error(`Failed to save data: ${err?.message}`);
      }
    });
}

export function getStatistics(db: Database, callback: (stats: Statistics) => void) {

  db.all('SELECT user, class, count(*) as count FROM collections GROUP BY user, class', (err, rows) => {
    if (err) {
      console.error(`Failed to query statistics: ${err.message}`);
    }
    let stats: Statistics = {};
    rows.forEach(row => {
      if (!stats[row.user]) {
        stats[row.user] = emptyUserStats;
      }
      stats[row.user] = { ...stats[row.user], [row.class]: row.count };
    });
    callback(stats);
  });
}